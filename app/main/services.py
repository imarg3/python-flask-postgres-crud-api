from app.main.repositories import UserRepository


class UserService:
    """
    Business logic and domain services.
    """
    @staticmethod
    def create_user(data):
        return UserRepository.create_user(data['username'], data['email'])

    @staticmethod
    def get_users():
        return UserRepository.get_all_users()

    @staticmethod
    def get_user(user_id):
        return UserRepository.get_user_by_id(user_id)

    @staticmethod
    def update_user(user_id, data):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            UserRepository.update_user(user, data['username'], data['email'])
        return user

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            UserRepository.delete_user(user)
        return user
