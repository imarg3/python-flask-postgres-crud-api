from app.main.services import UserService


def test_create_user(app):
    with app.app_context():
        user_data = {'username': 'testuser', 'email': 'test@example.com'}
        user = UserService.create_user(user_data)
        assert user.username == 'testuser'
        assert user.email == 'test@example.com'


def test_get_users(app):
    with app.app_context():
        users = UserService.get_users()
        assert isinstance(users, list)
