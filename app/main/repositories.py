from app.main.models import User
from app import db


class UserRepository:
    """
    Repositories for interacting with the database.
    """
    @staticmethod
    def create_user(username, email):
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.filter_by(id=user_id).first()

    @staticmethod
    def update_user(user, username, email):
        user.username = username
        user.email = email
        db.session.commit()

    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()
