Feature: Nesse arquivo estamos realizando fluxos basicos no site da C&A

  Scenario: Realizar login com email e senha
    Given que o usuário acessa o site da C&A
    When o usuário clica no botão de login
    And o usuário seleciona a opção "Entrar com email e senha"
    And o usuário preenche o email e a senha
    Then o login é realizado com sucesso

@wip
  Scenario Outline: Buscar diferentes produtos na barra de pesquisa
    Given que o usuário acessa o site da C&A
    When o usuário busca pelo produto "<produto>" na barra de pesquisa
    # Then o resultado da busca é exibido

    Examples:
      | produto     |
      | camiseta    |
      | calça jeans |
      | tênis       |