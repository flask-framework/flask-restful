"""
用户自定义资源
"""
from flask_restful import Resource
from utils.auth import jwt_required


class LoginResource(Resource):

    method_decorators = [jwt_required]
