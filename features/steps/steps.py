from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from my_secrets import get_email, get_senha

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

@step('o usuário busca pelo produto "{produto}" na barra de pesquisa')
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