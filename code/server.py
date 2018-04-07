from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT
from flask_restful import Api

from resources.user import User
from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:nigeriA070@localhost/fastPay'

api = Api(app)
CORS(app)

app.config['SECRET_KEY'] = 'fast_pay'
jwt = JWT(app, authenticate, identity)

api.add_resource(User, '/user')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host=0.0.0.0, port=5000, debug=True)
