from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from my_secrets import get_email, get_senha, get_senha_errada
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time


@step("que o usuário acessa o site da C&A")
def step_acessa_site(context):
    context.driver.get("https://www.cea.com.br/")

@step("o usuário clica no botão de login")
def step_clicka_login(context):
    context.driver.find_element(By.XPATH, "//div[contains(@class, 'cea-cea-store-theme-2-x-header-login')]").click()
    WebDriverWait(context.driver, 10).until(lambda d: "entre ou cadastre-se" in d.page_source.lower())
    context.driver.find_element(By.XPATH, "//div[text()='Entrar']").click()

@step("o usuário seleciona a opção \"Entrar com email e senha\"")
def step_seleciona_email_senha(context):
    assert WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h3[normalize-space(text())='Escolha uma opção para entrar']"))
    )
    context.driver.find_element(By.XPATH, "//h3[normalize-space(text())='Escolha uma opção para entrar']").click()

    WebDriverWait(context.driver, 30).until(lambda d: "Entrar com email e senha" in d.page_source)
    WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Entrar com email e senha']]"))
    ).click()

@step("o usuário preenche o email e a senha")
def step_preenche_credenciais(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Ex.: exemplo@mail.com']").send_keys(get_email())
    context.driver.find_element(By.XPATH, "//input[@placeholder='Adicione sua senha']").send_keys(get_senha())

@step("o login é realizado com sucesso")
def step_login_sucesso(context):
    botao_entrar = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Entrar']"))
    )
    botao_entrar.click()

    cliente = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'header-login__text-header') and contains(text(), 'Olá Cliente')]"))
    )
    assert cliente.is_displayed()

@step("o usuário desloga da aplicação")
def step_desloga_aplicacao(context):
    try:
        print("Validando se o texto 'Olá Cliente' está visível...")
        ola_cliente = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[@class='cea-cea-store-theme-2-x-header-login__text-header' and contains(text(), 'Olá Cliente')]"))
        )
        assert ola_cliente.is_displayed(), "Texto 'Olá Cliente' não encontrado."

        print("Clicando no botão 'Olá Cliente'...")
        ola_cliente.click()

        print("Verificando se o nome 'Cliente' está visível...")
        nome_cliente = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='cea-cea-store-theme-2-x-logged-container__name' and contains(text(), 'Cliente')]"))
        )
        assert nome_cliente.is_displayed(), "Nome 'Cliente' não exibido após clique."

        print("Clicando no link de sair da conta...")
        sair_link = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'logout') and contains(., 'sair desta conta')]"))
        )
        sair_link.click()
        print("Logout realizado com sucesso.")

    except Exception as e:
        raise Exception(f"[ERRO] Falha no processo de logout: {e}")

@step('o usuário busca pelo produto "{produto}" na barra de pesquisa e seleciona um produto exibido')
def step_busca_produto(context, produto):
    barra_pesquisa = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='aa-Input']"))
    )
    barra_pesquisa.clear()
    barra_pesquisa.send_keys(produto)
    produto = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//div[@class='aa-ItemContentTitle' and contains(text(), '{produto}')]"))
    )
    produto.click()

@step('o usuário busca pelo produto "{produto}" na barra de pesquisa e a listagem é exibida')
def step_busca_produto_alternativa(context, produto):
    barra_pesquisa = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='aa-Input']"))
    )
    barra_pesquisa.clear()
    barra_pesquisa.send_keys(produto)
    produto = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//div[@class='aa-ItemContentTitle' and contains(text(), '{produto}')]"))
    )
    barra_pesquisa.send_keys(Keys.ENTER)
    time.sleep(1)

@step('o resultado da busca pelo {produto} é exibido')
def step_valida_resultado_nome(context, produto):
    elemento = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//h1[contains(@class, 'cea-cea-store-theme-2-x-product-title')]")))
    assert elemento.is_displayed(), f"Elemento não encontrado: {elemento}"

@step('o usuário seleciona o tamanho "{tamanho}"')
def step_seleciona_tamanho(context, tamanho):
    tamanho_element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,f"//div[contains(@class, 'skuSelectorItemTextValue') and normalize-space(text())='{tamanho}']")))
    tamanho_element.click()

@step('o usuário seleciona a cor "{cor}"')
def step_seleciona_cor(context, cor):
    if not cor or not cor.strip():
        print("Cor não informada, pulando seleção.")
        return

    try:
        print(f"Selecionando cor: {cor}")
        cor_element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                f"//span[contains(@class, 'tooltip__message') and normalize-space(text())='{cor.lower()}']"
            ))
        )
        cor_element.click()
        time.sleep(1)
    except Exception as e:
        raise Exception(f"Erro ao selecionar a cor '{cor}': {e}")


@step('a listagem com o "{produto}" é exibida')
def step_listagem_com_produto_exibida(context, produto):
    try:
        time.sleep(3)
        count = context.driver.page_source.lower().count(produto.lower())

        if count > 0:
            print(f"O produto '{produto}' foi encontrado {count} vez(es) na página.")
        else:
            raise Exception(f"O produto '{produto}' NÃO foi encontrado.")
    except Exception as e:
        raise Exception(f"Erro ao verificar listagem: {e}")


@step('o usuário clica no primeiro produto exibido')
def step_clica_no_primeiro_produto(context):
    try:
        WebDriverWait(context.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Encontrar similares']"))
        )
        print('"Encontrar similares" encontrado na tela.')

        primeiro_item = WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class, 'ais-image isHover')])[1]"))
        )
        primeiro_item.click()
        print("Clique no primeiro produto realizado com sucesso.")

    except Exception as e:
        raise Exception(f"Erro ao clicar no primeiro produto exibido: {e}")


@step('adiciona o produto à sacola de compras')
def step_adiciona_produto_sacola(context):
    try:
        adicionar_btn = WebDriverWait(context.driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Adicionar à sacola')]"))
        )
        adicionar_btn.click()
        print("Clique no botão 'Adicionar à sacola' realizado com sucesso.")

        WebDriverWait(context.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//h3[contains(@class, 'minicart-title__header') and contains(text(), 'Resumo da sacola')]"))
        )
        print("Resumo da sacola exibido com sucesso.")

    except Exception as e:
        raise Exception(f"Erro ao adicionar o produto à sacola: {e}")
    
@step('o usuário fecha a sacola de compras')
def fecha_sacola(context):
        fechar_btn = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'vtex-minicart-2-x-closeIconButton')]"))).click()

        print("Sacola de compras fechada com sucesso.")


@step('o usuário remove itens da sacola')
def step_remover_todos_os_items(context):
    try:
        botoes_remover = WebDriverWait(context.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[starts-with(@id, 'remove-button-')]"))
        )

        for botao in botoes_remover:
            WebDriverWait(context.driver, 10).until(
                EC.element_to_be_clickable(botao)
            ).click()

        print("Todos os itens foram removidos da sacola.")

        WebDriverWait(context.driver, 15).until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//span[contains(text(), 'Sua sacola ainda está vazia')]"
            ))
        )
        print("Confirmação: Sacola vazia exibida.")

    except Exception as e:
        raise Exception(f"Erro ao remover os itens da sacola ou verificar sacola vazia: {e}")
    
@step("o usuário preenche um email válido e uma senha incorreta")
def step_email_senha_incorreta(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Ex.: exemplo@mail.com']").send_keys(get_email())
    context.driver.find_element(By.XPATH, "//input[@placeholder='Adicione sua senha']").send_keys(get_senha_errada())

@step("uma mensagem de erro de login é exibida")
def step_valida_erro_login(context):
    botao_entrar = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Entrar']"))
    )
    botao_entrar.click()
    
    erro_msg = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//div[contains(@class, 'vtex-login-2-x-formError') and contains(text(), 'Usuário e/ou senha incorretos')]"
        ))
    )
    assert erro_msg.is_displayed(), "Mensagem de erro de login não exibida"
