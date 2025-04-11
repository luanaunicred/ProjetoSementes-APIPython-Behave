import requests
from PetStore.config import base_url

data = {
  'id': 0,
  'username': 'luana_souza',
  'firstName': 'Luana',
  'lastName': 'Souza',
  'email': 'luana.souza@unicred.com.br',
  'password': '123456',
  'phone': '51998085898',
  'userStatus': 1
}

def test_criar_usuario():
    url_post = f'{base_url}/user'

    response = requests.post(url_post, json=data)

    print("STATUS CODE:", response.status_code)
    print("RESPOSTA:", response.text)

    assert response.status_code == 200

    json_data = response.json()
    assert 'code' in json_data
    assert json_data["type"] == "unknown"