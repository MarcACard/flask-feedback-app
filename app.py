from flask import Flask, redirect, render_template, flash, session
from models import connect_db, db, User, Feedback
from forms import RegistrationForm, LoginForm, FeedbackForm


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///feedback"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECH"] = True
app.config["SECRET_KEY"] = "aBcDeF12345"

connect_db(app)


@app.route("/")
def home():

    if "username" in session:
        return redirect(f"/users/{session['username']}")

    return redirect("/register")


@app.route("/register", methods=["GET", "POST"])
def user_registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        new_user = User.register(
            username=form.username.data,
            password=form.password.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
        )

        db.session.add(new_user)
        db.session.commit()
        session["username"] = new_user.username

        flash("Thanks for Registering")
        return redirect(f"/users/{new_user.username}")

    return render_template("registration.html", form=form)


###################
### USER ROUTES ###
###################


@app.route("/login", methods=["GET", "POST"])
def login_user():
    """Login Route"""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(
            username=form.username.data, password=form.password.data
        )
        if user:
            session["username"] = user.username
            flash("Welcome Back!")
            return redirect(f"/users/{user.username}")
        else:
            form.username.errors = ["Invalid Username/Password"]

    return render_template("login.html", form=form)


@app.route("/logout")
def logout_user():
    """Logout a user - remove username from session."""
    session.pop("username")
    flash("You've Successfully Been Logged Out")
    return redirect("/")


@app.route("/users/<username>")
def user_profile(username):
    """Display a user profile.
    -- Users will only be able to see their own profile.
    -- Attempted access to other will redirect to their own profile.
    """

    if "username" not in session:
        flash("You Must Be Registered and Logged in to View Profiles", "warning")
        return redirect("/register")

    if session["username"] != username:
        flash("Users May only View their Own Profile.", "warning")
        return redirect(f"/users/{session['username']}")

    user = User.query.get_or_404(username)
    feedback = Feedback.query.filter_by(username=user.username).all()

    return render_template("profile.html", user=user, feedback=feedback)


@app.route("/users/<username>/delete", methods=["POST"])
def delete_user(username):
    """Delete a user.
    -- Users Will Only be Able to delete their own profiles.
    """

    if "username" not in session:
        flash("You must be logged in to perform that action.")
    elif session["username"] != username:
        flash("Only a the owning user can delete their profile")
    else:
        user = db.session.query(User).filter(User.username == username).first()
        db.session.delete(user)
        db.session.commit()
        session.pop("username")
        flash("User and Related Data have been Deleted")

    return redirect("/")


############################
### USER FEEDBACK ROUTES ###
############################


@app.route("/users/<username>/feedback/add", methods=["GET", "POST"])
def add_feedback(username):
    """Display and Process a user feedback form."""

    form = FeedbackForm()

    if username != session["username"]:
        flash("You can only submit feedback from your profile.", "warning")
        return redirect("/users/{session['username']}")

    if form.validate_on_submit():
        feedback = Feedback(
            title=form.title.data,
            content=form.content.data,
            username=username,
        )
        db.session.add(feedback)
        db.session.commit()

        flash("Thanks for the feedback")
        return redirect(f"/users/{username}")

    return render_template("add_feedback.html", form=form)


#######################
### FEEDBACK ROUTES ###
#######################


@app.route("/feedback/<int:feedback_id>/update", methods=["GET", "POST"])
def update_feedback(feedback_id):
    """Display feedback form update user and process on resubmission.
    -- Users will only be allowed to edit their own feedback.
    -- Unauthorized access will be redirected to homepage or their own user profile.

    """

    feedback = Feedback.query.get_or_404(feedback_id)
    username = feedback.username
    form = FeedbackForm(obj=feedback)

    if username != session["username"]:
        flash("Only the owning user can edit feedback.", "warning")
        return redirect("/users/{session['username']}")

    if form.validate_on_submit():
        form.populate_obj(feedback)
        db.session.commit()

        flash("Feedback has been updated")
        return redirect(f"/users/{username}")

    return render_template("update_feedback.html", form=form)


@app.route("/feedback/<int:feedback_id>/delete", methods=["POST"])
def delete_feedback(feedback_id):
    """Delete a users feedback.
    -- Users Will Only be Able to delete their own feedback.
    """

    feedback = Feedback.query.get_or_404(feedback_id)

    if "username" not in session:
        flash("You must be logged in to perform that action.")
    elif session["username"] != feedback.username:
        flash("Only a the owning user can delete their feedback")
    else:
        db.session.delete(feedback)
        db.session.commit()
        flash("Feedback has been deleted")

    return redirect("/")
