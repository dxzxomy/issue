from backend.ext import db
from datetime import datetime
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(30), unique=True)
    create_time = db.Column(db.DateTime,default=datetime.now)
    last_login = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean,default=True)
    is_surperuser = db.Column(db.Boolean, default=False)

    def __str__(self):
        return self.username