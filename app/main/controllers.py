"""
API endpoints.
"""

from flask import Blueprint, jsonify, request, make_response
from app.main.services import UserService

main_bp = Blueprint('main', __name__)


@main_bp.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'test route'}), 200)


@main_bp.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        user = UserService.create_user(data)
        return make_response(jsonify({'message': 'user created', 'user': user.json()}), 201)
    except Exception as e:
        return make_response(jsonify({'message': f'error creating user: {str(e)}'}), 500)


@main_bp.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_users()
    return make_response(jsonify([user.json() for user in users]), 200)


@main_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = UserService.get_user(id)
    if user:
        return make_response(jsonify({'user': user.json()}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)


@main_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        data = request.get_json()
        user = UserService.update_user(id, data)
        if user:
            return make_response(jsonify({'message': 'user updated'}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': f'error updating user: {str(e)}'}), 500)


@main_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = UserService.delete_user(id)
        if user:
            return make_response(jsonify({'message': 'user deleted'}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': f'error deleting user: {str(e)}'}), 500)
