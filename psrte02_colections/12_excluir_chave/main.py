# Biblioteca
import os

# dicionário
usuario = {
    'nome': "Ekire",
    'idade': 23,
    'email': "ekire@gmail.com",
    'telefone': "(61) 940028922",
    'endereço': "Campo da Esperança"
}

# Exibe a lista original
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")

# Informa a chave a ser deletada
chave_escolhida = input("Informe a chave a excluir: ").strip().lower()

# Deleta a chave
del usuario[chave_escolhida]

# re-exibe o novo dicionário
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")