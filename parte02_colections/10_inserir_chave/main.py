# dicionário
usuario = {
    'nome': "Ekire",
    'idade': 23,
    'email': "Ekire@gmail.com"
}

# Usuário infromar o nome da nova chave
nova_chave = input("Informe o nome da nova chave: ").strip().lower()
# Usuário informa o valor da nova chave
usuario[nova_chave] = input("Informe o valor da nova chave: ").strip()

# Exibir o dicionário
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}.")