import requests
from config import base_url


def test_atualiza_usuario():
    username = 'luana_souza'
    url_put = f'{base_url}/user/{username}'

    data_updated = {
        'id': 0,
        'username': 'luana_souza',
        'firstName': 'Luana',
        'lastName': 'Acosta',
        'email': 'luana.acosta@gmail.com',
        'password': 'Uni123',
        'phone': '5198085898',
        'userStatus': 1
    }

    response = requests.put(url_put, json=data_updated)

    print('STATUS CODE: ', response.status_code)
    print('RESPOSTA', response.text)

    assert response.status_code == 200

    url_get = f'{base_url}/user/{username}'
    response_get = requests.get(url_get)

    print('GET STATUS CODE: ', response_get.status_code)
    print('GET RESPOSTA: ', response_get.text)

    assert response_get.status_code == 200
    json_get = response_get.json()

    assert json_get['firstName'] == data_updated['firstName']
    assert json_get['lastName'] == data_updated['lastName']
    assert json_get['email'] == data_updated['email']
    assert json_get['phone'] == data_updated['phone']