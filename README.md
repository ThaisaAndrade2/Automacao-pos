
# 🧪 Automação de Testes com Behave + Selenium + Playwright

Este projeto utiliza `Behave` com `Selenium` e `Playwright` para automação de testes no site da C&A.

---

## ✅ 1. Instalação de dependências e navegadores Playwright

Execute os comandos abaixo para instalar todas as dependências necessárias:

```bash
python -m pip install -r requirements.txt
playwright install
```

---

## 🔐 2. Configuração da senha (arquivo `my_secrets.py`)

Para proteger suas credenciais, usamos um arquivo chamado `my_secrets.py`, que **não está no repositório** por segurança.

### Passos:

1. Copie o arquivo de exemplo:

```bash
cp my_secrets_example.py my_secrets.py
```

---

## 🚀 3. Comandos para execução dos testes

### ✅ Executar apenas os cenários principais:

```bash
python -m behave features/scenarios.feature
```

### 🔐 Executar apenas os testes de login:

```bash
python -m behave login.feature
```

### 🧪 Executar todos os testes disponíveis:

```bash
python -m behave
```
