from models import db, User, Feedback
from app import app

db.drop_all()
db.create_all()

# Sample User
user1 = User.register(
    username="test",
    password="password",
    email="test@gmail.com",
    first_name="John",
    last_name="Smith",
)

db.session.add(user1)
db.session.commit()

## Add sample feedback to test user.
fb1 = Feedback(
    title="Feedback 1",
    content="Short amount of feedback provided by the users. Sample content",
    username="test",
)
fb2 = Feedback(
    title="Feedback 2",
    content=" Integer ut rutrum ante. Nullam id iaculis neque, eu accumsan metus. Integer consequat leo vitae egestas tincidunt. Donec mollis vitae ipsum nec efficitur. Morbi purus leo, posuere non enim a, iaculis mattis libero. Donec malesuada ullamcorper dui at semper. Nulla at malesuada ipsum, nec cursus neque. Morbi gravida euismod dui, at posuere quam feugiat id. Nullam non dolor non augue commodo finibus. Aenean at convallis neque, eu ullamcorper arcu. Duis vitae vehicula purus. Duis eu leo ac tellus sagittis faucibus. In eros neque, pellentesque sit amet ex sit amet, ultricies tristique massa. Maecenas nisi urna, imperdiet eget elit ut, congue euismod leo. Etiam non turpis eget sapien ultrices consequat. ",
    username="test",
)
fb3 = Feedback(
    title="Feedback 3",
    content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam ut finibus sem. Donec ullamcorper eget ipsum vel vestibulum. Cras ornare, odio eget consequat posuere, sapien ligula luctus arcu, quis sodales ipsum lacus id justo. Duis nec imperdiet augue. Vivamus rhoncus ipsum leo, non tempus ex molestie nec. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Quisque ornare enim vitae ex porta, at dictum dui porttitor. Nam condimentum blandit arcu, iaculis pellentesque tellus. Proin arcu metus, interdum et risus ut, commodo varius dui. Nunc porta mauris vel dictum semper. Cras molestie dignissim ipsum et vestibulum. Integer ut rutrum ante. Nullam id iaculis neque, eu accumsan metus. Integer consequat leo vitae egestas tincidunt. Donec mollis vitae ipsum nec efficitur. Morbi purus leo, posuere non enim a, iaculis mattis libero. Donec malesuada ullamcorper dui at semper. Nulla at malesuada ipsum, nec cursus neque. Morbi gravida euismod dui, at posuere quam feugiat id. Nullam non dolor non augue commodo finibus. Aenean at convallis neque, eu ullamcorper arcu. Duis vitae vehicula purus. Duis eu leo ac tellus sagittis faucibus. In eros neque, pellentesque sit amet ex sit amet, ultricies tristique massa. Maecenas nisi urna, imperdiet eget elit ut, congue euismod leo. Etiam non turpis eget sapien ultrices consequat. ",
    username="test",
)
fb4 = Feedback(
    title="Feedback 4",
    content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam ut finibus sem. Donec ullamcorper eget ipsum vel v",
    username="test",
)
db.session.add_all([fb1, fb2, fb3, fb4])
db.session.commit()
