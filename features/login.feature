Feature: Nesse arquivo estamos logins happy

  @HappyFlow 
  Scenario: Realizar login com email e senha
    Given que o usuário acessa o site da C&A
    When o usuário clica no botão de login
    And o usuário seleciona a opção "Entrar com email e senha"
    And o usuário preenche o email e a senha
    Then o login é realizado com sucesso

  @UnhappyFlow @wip
  Scenario: Tentativa de login com email e senha incorretos
    Given que o usuário acessa o site da C&A
    And o usuário clica no botão de login
    And o usuário seleciona a opção "Entrar com email e senha"
    When o usuário preenche um email válido e uma senha incorreta
    Then uma mensagem de erro de login é exibida