import base64

email = "seuemail@exemplo.com"
senha_criptografada = base64.b64encode("suaSenha123".encode()).decode()

def get_email():
    return email

def get_senha():
    return base64.b64decode(senha_criptografada.encode()).decode()