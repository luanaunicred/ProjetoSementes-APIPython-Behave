import requests
from config import base_url


def test_consulta_usuario():
    username = 'luana_souza'
    url_get = f'{base_url}/user/{username}'

    response = requests.get(url_get)

    print('STATUS CODE: ', response.status_code)
    print('RESPOSTA', response.text)

    assert response.status_code == 200

    json_data = response.json()

    assert json_data['username'] == 'luana_souza'
    assert json_data['email'] == 'luana.souza@unicred.com.br'
    assert json_data['firstName'] == 'Luana'
    assert json_data['lastName'] == 'Souza'