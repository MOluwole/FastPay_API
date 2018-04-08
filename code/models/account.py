from db import db
import pymysql


class Account(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100))
    balance = db.Column(db.String(100))

    def __init__(self, user_id, balance):
        self.user_id = user_id
        self.balance = balance

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()

    def save_user_account(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def update_account(cls, user_id, balance):
        account_details = cls.query.filter_by(user_id=user_id).first()
        account_details.balance = balance
        db.session.commit()
