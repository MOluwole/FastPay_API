from flask_restful import Resource, reqparse
from models.transaction import Transaction as TransactionModel
from models.account import Account

class Transaction(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('transaction_type', type=str)
    parser.add_argument('sender', type=str)
    parser.add_argument('receiver', type=str)
    parser.add_argument('transaction_details', type=str)
    parser.add_argument('amount', type=str)

    def post(self):
        data = Transaction.parser.parse_args()

        type_ = data['transaction_type']
        sender = data['sender']
        receiver = data['receiver']
        details = data['transaction_details']
        amount = data['amount']

        transaction = TransactionModel(type_, sender, receiver, amount, details)

        sender_account = Account.find_by_user_id(sender)
        receiver_account = Account.find_by_user_id(receiver)

        if sender_account:
            balance = int(str(sender_account.balance))
            int_amount = int(str(amount))

            if balance < int_amount:
                return {'message': 'Insufficient Balance'}, 400

            new_balance = balance - int_amount
            Account.update_account(sender, new_balance)

            if receiver_account:
                receiver_balance = int(str(receiver_account.balance))
                receiver_new_balance = receiver_balance + int_amount
                Account.update_account(receiver, receiver_new_balance)

            transaction.save_transaction()

            return {'message': 'Transaction saved successfully'}, 201

        return {'message': "No Account has been Associated with this User ID"}, 400

    def get(self):
        data = Transaction.parser.parse_args()

        if data['sender'] is not None:
            user_id = data['sender']
        else:
            user_id = data['receiver']

        transaction = TransactionModel.find_transaction(user_id)

        transaction_data = []
        for item in transaction:
            single_data = TransactionModel.return_json(item.type_, item.sender, item.receiver, item.amount, item.transaction_details, item.transaction_date, item.transaction_time)
            transaction_data.append(single_data)
        # transaction = TransactionModel.query.filter((TransactionModel.sender) | (TransactionModel.receiver))

        if transaction:
            return {'data': transaction_data}, 200
        else:
            return {"message": "No Transaction yet"}, 404
