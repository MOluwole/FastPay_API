from flask_restful import Resource, reqparse
from models.user import User as UserModel

class User(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('username', type=str, required=True, help="Username is Required")
    parser.add_argument('password', type=str, required=True, help="Password is required")
    parser.add_argument('email_id', type=str)
    parser.add_argument('phone_num', type=str)

    def post(self):
        data = User.parser.parse_args()

        username = data['username']
        password = data['password']
        email_id = data['email_id']
        phone_num = data['phone_num']

        user = UserModel.find_by_username(username)
        if user:
            return {'message': "Username exists. Provide a unique username to proceed"}, 400

        user_details = UserModel(username, password, email_id, phone_num)

        user_details.save_user()
        return {'message': 'User Created Successful'}, 201
