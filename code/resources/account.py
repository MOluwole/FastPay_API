from flask_restful import Resource, reqparse
from models.account import Account as AccountModel

class Account(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('user_id', type=str)
    parser.add_argument('balance', type=str)

    def post(self):
        data = Account.parser.parse_args()

        user_id = data['user_id']
        balance = data['balance']

        user = AccountModel.find_by_user_id(user_id)
        if user:
            AccountModel.update_account(user_id, balance)
            return {"message": "Account Update Successful"}, 201

        user_account = AccountModel(user_id, balance)
        user_account.save_user_account()

        return {"message": "Account Creation Successful"}, 201

    def get(self):
        data = Account.parser.parse_args()

        user_id = data['user_id']

        user = AccountModel.find_by_user_id(user_id)
        if user:
            return {"data": user}, 200
        else:
            return {"message": "No Account Associated yet"}, 404
