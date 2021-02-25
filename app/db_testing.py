from app.models import db, User

db.drop_all()
db.create_all()
user = User(id=1, email='email@domain.com', password=123)
db.session.add(user)
db.session.commit()