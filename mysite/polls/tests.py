import requests


def test_login_to_django_dashboard():
    url = 'http://127.0.0.1:8000/admin/login/'
    response_0 = requests.get(url)
    csrftoken = response_0.cookies['csrftoken']
    username = 'admin'
    password = 'admin2020'
    login_data = {'username': username, 'password': password, 'csrfmiddlewaretoken': csrftoken, 'next': '/admin/'}
    response = requests.post(url, data=login_data, cookies=response_0.cookies)
    print(response.text)
    assert response.status_code == 200
    assert response.url == 'http://127.0.0.1:8000/admin/'
