# Lista de dicionários
usuarios = [
    {
        'nome': "Ekure-san", 
        'idade': 23,
        'email': "Ekuresan@gmail.com"
    },
    {
        'nome': "Mizuko-chan",
        'idade': 16,
        'email': "Mizukochan@gmail.com"
    },
    {
        'nome': "Minato-san",
        'idade': 35,
        'email': "Minatosan@gmail.com"
    }
]

# Exibe os dados de todos os usuários
for usuario in usuarios:
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    print(f"{'-'*40}")