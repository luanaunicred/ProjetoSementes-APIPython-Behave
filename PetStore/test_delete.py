import requests
from PetStore.config import base_url



def teste_deletar_usuario():
    username = 'luana_souza'
    url_delete = f'{base_url}/user/{username}'

    response = requests.delete(url_delete)

    print('STATUS CODE (DELETE): ', response.status_code)
    print('RESPOSTA (DELETE): ', response.text)

    assert response.status_code == 200

    response_get  =requests.get(f'{base_url}/user/{username}')

    print('STATUS CODE (GET após DELETE):', response_get.status_code)
    print('RESPOSTA (GET após DELETE):', response_get.text)

    assert response_get.status_code == 404