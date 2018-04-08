import pymysql
from db import db
from datetime import datetime

class Transaction(db.Model):
    __tablename__ = "transaction"

    id = db.Column(db.Integer, primary_key=True)
    type_ = db.Column(db.Integer)
    sender = db.Column(db.String(100))
    receiver = db.Column(db.String(100))
    amount = db.Column(db.String(100))
    transaction_details = db.Column(db.String(100))
    transaction_date = db.Column(db.String(100))
    transaction_time = db.Column(db.String(100))

    def __init__(self, type_, sender, receiver, amount, transaction_details):
        self.type_ = type_
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.transaction_details = transaction_details

        dte = datetime.now()
        date = "%02d-%02d-%02d" % (dte.year, dte.month, dte.day)
        time = "%02d:%02d:%02d" % (dte.hour, dte.minute, dte.second)

        self.transaction_time = time
        self.transaction_date = date

    @classmethod
    def return_json(cls, type_, sender, receiver, amount, transaction_details, transaction_date, transaction_time):
        return {'type_': type_, 'sender': sender, 'receiver': receiver, 'amount': amount, 'transaction_details': transaction_details, 'transaction_date': transaction_date, 'transaction_time': transaction_time}

    @classmethod
    def find_transaction(cls, user_id):
        return cls.query.filter((cls.sender==user_id) | (cls.receiver==user_id)).all()

    def save_transaction(self):

        db.session.add(self)
        db.session.commit()
