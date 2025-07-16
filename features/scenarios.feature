Feature: Nesse arquivo estamos realizando fluxos basicos no site da C&A para a pós Gradução do curso de Automação de Testes

  @HappyFlow
  Scenario Outline: Buscar diferentes produtos na barra de pesquisa
    Given que o usuário acessa o site da C&A
    When o usuário busca pelo produto "<produto>" na barra de pesquisa e seleciona um produto exibido
    Then o resultado da busca pelo "<produto>" é exibido

    Examples:
      | produto  |
      | camiseta |
      | vestido  |

  @HappyFlow
  Scenario Outline: Buscar produto expecifico na listagem na barra de pesquisa e adicionando a sacola de compras
    Given que o usuário acessa o site da C&A
    And o usuário busca pelo produto "<produto>" na barra de pesquisa e a listagem é exibida
    And a listagem com o "<produto>" é exibida
    When o usuário clica no primeiro produto exibido
    And o usuário seleciona o tamanho "<tamanho>"
    Then adiciona o produto à sacola de compras
    And o usuário fecha a sacola de compras

    Examples:
      | produto                                                | tamanho |
      | camiseta feminina de algodão born in the 90s off white | P       |

  @HappyFlow
  Scenario Outline: Remover produtos da sacola de compras
    Given que o usuário acessa o site da C&A
    And o usuário busca pelo produto "<produto>" na barra de pesquisa e a listagem é exibida
    And a listagem com o "<produto>" é exibida
    When o usuário clica no primeiro produto exibido
    And o usuário seleciona o tamanho "<tamanho>"
    And adiciona o produto à sacola de compras
    Then o usuário remove itens da sacola

    Examples:
      | produto                                         | tamanho |
      | short saia de sarja cintura alta com fenda rosa | 42      |

  @HappyFlow
  Scenario Outline: Fluxo completo login e sacola de compras
    Given que o usuário acessa o site da C&A
    And o usuário clica no botão de login
    And o usuário seleciona a opção "Entrar com email e senha"
    And o usuário preenche o email e a senha
    When o login é realizado com sucesso
    And o usuário busca pelo produto "<produto>" na barra de pesquisa e a listagem é exibida
    And a listagem com o "<produto>" é exibida
    And o usuário clica no primeiro produto exibido
    And o usuário seleciona o tamanho "<tamanho>"
    And adiciona o produto à sacola de compras
    And o usuário fecha a sacola de compras

    Examples:
      | produto                                       | tamanho |
      | blusa de viscose gola alta listrada off white | P       |
