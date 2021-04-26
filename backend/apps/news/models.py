from backend.ext import db
from datetime import datetime
class News(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(99), nullable=False)
    url = db.Column(db.String(99), nullable=False)
    ctime = db.Column(db.String(30), nullable=False)

    # def __str__(self):
    #     return self.username