import pymysql
from db import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email_id = db.Column(db.String(100))
    phone_num = db.Column(db.String(100))
    created_at = db.Column(db.String(100))

    def __init__(self, user_id, password, email_id, phone_num):
        self.user_id = user_id
        self.password = password
        self.email_id = email_id
        self.phone_num = phone_num

        dte = datetime.now()

        self.date = "%02d-%02d-%02d" % (dte.year, dte.month, dte.day)
        self.time = "%02d:%02d:%02d" % (dte.hour, dte.minute, dte.second)

        self.created_at = self.date + " " + self.time


    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()

    def find_by_email(cls, email_id):
        return cls.query.filter_by(email_id=email_id).first()

    def save_user(self):
        db.session.add(self)
        db.session.commit()
