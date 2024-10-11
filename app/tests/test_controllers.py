def test_create_user(client):
    response = client.post('/users', json={'username': 'testuser', 'email': 'test@example.com'})
    assert response.status_code == 201
    assert response.get_json()['message'] == 'user created'


def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
