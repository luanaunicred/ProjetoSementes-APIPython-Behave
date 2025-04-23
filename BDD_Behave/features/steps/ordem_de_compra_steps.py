from behave import *
from BDD_Behave.features.impl.ordem_de_compra import OrdemDeCompra

@given(u'que o usuário selecionou o animal com o id correspondente a "{id}" desejado na petstore')
def step_impl(context,id):  #inclui id
    context.ordem = OrdemDeCompra()
    context.ordem.id = id #alterei 1 para id
    context.ordem.petId = 2
    context.ordem.quantidade = 10
    context.ordem.post_criar_uma_nova_ordem()


@then(u'o sistema valida se a ordem de pedido foi armazenada corretamente')
def step_impl(context):
    response = context.ordem.get_consultar_ordem_de_compra(context.ordem.id)
    assert response.status_code == 200, f"Status code esperado: 200, obtido: {response.status_code}"

    data = context.ordem.response_data
    assert data['id'] == context.ordem.id, f"ID esperado: {context.ordem.id}, obtido: {data['id']}"
    assert data['petId'] == context.ordem.petId, f"petId esperado: {context.ordem.petId}, obtido: {data['petId']}"
    assert data['quantity'] == context.ordem.quantidade, f"Quantidade esperada: {context.ordem.quantidade}, obtido: {data['quantity']}"
    assert data['status'] == "placed", f"Status esperado: placed, obtido: {data['status']}"
    assert data['complete'] == True, f"Complete esperado: True, obtido: {data['complete']}"