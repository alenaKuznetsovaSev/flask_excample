from app import db
from app.models import User, Post
# u = User(username='al', email='al@gmail.com')
# print(u)
# db.session.add(u)
# db.session.commit()
# print(User.query.all())
# u = User(username='max', email='max@gmail.com')
# print(u)
# db.session.add(u)
# db.session.commit()
for u in User.query.all():
    db.session.delete(u)
db.session.commit()