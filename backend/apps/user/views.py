from flask import Blueprint
from flask_restful import Resource
from ext import api

user_bp = Blueprint('user', __name__, url_prefix='/api')

# @user_bp.route('/')
# def usercenter():
#     return '用户中心'
#
#
# @user_bp.route('/register', methods=['GET', 'POST'])
# def register():
#     return '注册'

class UserResource(Resource):

    def get(self):
        return 'get'

    def post(self):

        return 'post'

    def put(self):

        return 'put'

    def delete(self):
        return 'delete'

    def patch(self):

        return 'patch'

api.add_resource(UserResource, '/user')