Feature: Gerenciamento de usuários via API PetStore
  Scenario: Criar usuário com POST
    When eu envio uma requisição POST com os dados
    """
    [
      {
        "id": 12345,
        "username": "lulu",
        "firstName": "Luana",
        "lastName": "Acosta",
        "email": "luana.acosta@email.com",
        "password": "123456",
        "phone": "51999999999",
        "userStatus": 1
        }
    ]
    """

    Then o status code deve ser 200
    And o campo "message" da resposta deve ser "ok"

  Scenario: Consultar usuário com GET
    When eu envio uma requisição GET para o usuário "lulu"
    Then o status code deve ser 200
    And o campo "username" da resposta deve ser "lulu"

  Scenario: Atualizar usuário com PUT
    When eu envio uma requisição PUT para o usuário "lulu" com os dados
      """
      {
        "id": 12345,
        "username": "lulu",
        "firstName": "Luana Acosta",
        "lastName": "Souza",
        "email": "luacosta@email.com",
        "password": "987654",
        "phone": "51998085898",
        "userStatus": 1
      }
      """
    Then o status code deve ser 200

  Scenario: Deletar usuário com DELETE
    When eu envio uma requisição DELETE para o usuário "lulu"
    Then o status code deve ser 200