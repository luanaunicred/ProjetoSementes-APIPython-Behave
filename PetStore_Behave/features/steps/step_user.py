from behave import when, then
import json
from PetStore_Behave.features.impl import user_api

@when('eu envio uma requisição POST com os dados')
def step_impl_post_user(context):
    users = json.loads(context.text)
    context.response = user_api.post_user(users)

@when('eu envio uma requisição GET para o usuário "{username}"')
def step_impl_get_user(context, username):
    context.response = user_api.get_user(username)

@when('eu envio uma requisição PUT para o usuário "{username}" com os dados')
def step_impl_put_user(context, username):
    data = json.loads(context.text)
    context.response = user_api.put_user(username, data)

@when('eu envio uma requisição DELETE para o usuário "{username}"')
def step_impl_delete_user(context, username):
    context.response = user_api.delete_user(username)

@then('o status code deve ser {status_code:d}')
def step_impl_validate_status_code(context, status_code):
    assert context.response.status_code == status_code, \
        f"Esperado {status_code}, mas retornou {context.response.status_code}"

@then('o campo "{campo}" da resposta deve ser "{valor}"')
def step_impl_validate_response_field(context, campo, valor):
    response_json = context.response.json()
    assert response_json.get(campo) == valor, \
        f'Campo "{campo}" esperado: "{valor}", recebido: "{response_json.get(campo)}"'