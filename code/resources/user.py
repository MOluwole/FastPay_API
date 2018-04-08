from flask_restful import Resource, reqparse
from models.user import User as UserModel

class User(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('user_id', type=str, required=True, help="User ID is Required")
    parser.add_argument('password', type=str, required=True, help="Password is required")
    parser.add_argument('email_id', type=str)
    parser.add_argument('phone_num', type=str)

    def post(self):
        data = User.parser.parse_args()

        username = data['user_id']
        password = data['password']
        email_id = data['email_id']
        phone_num = data['phone_num']

        user = UserModel.find_by_user_id(username)
        if user:
            return {'message': "User ID exists. Provide a unique User ID to proceed"}, 400

        user_details = UserModel(username, password, email_id, phone_num)

        user_details.save_user()
        return {'message': 'User Created Successful'}, 201
