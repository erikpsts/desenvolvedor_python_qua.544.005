# Feito: parte 02 atividade 01
"""
Crie um programa que faça as seguintes operações:
- Cadastra novo usuário (nome, email, telefone, cpf)
- Lista todos os usuários cadastrados
- Altera os dados de um usuário
- Exclui um usuário
- Grava os dados de todos os usuários em um .json
- Abre arquivo .json e lista todos os usuários cadastrados nele
"""

# Bibliotecas
import json
import os

# lista
usuarios = []

# limpa terminal
os.system("cls" if os.name == "nt" else "clear")

# loop
while True:
    # menu 
    print("1 - Cadastrar novo usuário") # Feito
    print("2 - Listar usuários cadastrados") # Feito
    print("3 - Alterar dados do usuário") # A melhorar
    print("4 - Excluir um usuário") # Feito
    print("5 - Gravar todod os usuários em  .json") # Feito
    print("6 - Abrir arquivo .json") # Feito
    print("7 - Sair do programa") # Feito
    opcao = input("Opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:

        # Cadastra novo usuário (Feito)
        case "1":
            # inicializar um novo dicionário
            usuario = {}
           
            # informa um novo usuário
            usuario['nome'] = input("Informe o nome: ").strip().title()
            usuario['email'] = input("Informe o e-mail: ").strip().lower()
            usuario['telefone'] = input("Informe o telefone: ").strip()
            usuario['cpf'] = input("Informe o CPF: ").strip()
           
            # adiciona novo usuário na lista
            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")
           
            # mensagem de confirmação
            print(f"{usuario.get('nome')} cadastrado com sucesso.")
            continue
        # Listar usuários cadastrados (Feito)
        case "2":
            if usuarios:    
                # exibe os usuários cadastrados
                for i, usuario in enumerate(usuarios):
                    print(f"TD: {i}")
                    for chave, valor in usuario.items():
                        print(f"{chave.capitalize()}: {valor}")
                    print(f"{'-'*40}")
            else:
                print("Não foram encontrados usuários cadastrados.")
            continue
        # Alterar dados de um usuário (Feito)
        case "3":
            try:
                indice = int(input("Informe o ID do usuário a atualizar: "))
                for chave, valor in usuarios[indice].items():
                    print(f"{chave.capitalize()} {valor}.")
                chave = input("Qual chave deseja alterar o valor? ").strip().lower()
                usuarios[indice][chave] = input("Informe o novo valor: ").strip()
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Dados de {usuarios[indice].get('nome')} alterado com sucesso!")
                continue
            except Exception as e:
                print(f"Não foi possível atualizar os dados. {e}")
        # Excluir um usuário (Feito)
        case "4":
            try:
                indice = int(input("Informe o ID a ser excluído: "))
                del usuarios[indice]
                os.system("cls" if os.name == "nt" else "clear")
                print("Usuário excluído com sucesso.")
                continue
            except Exception as e:
                print(f"Não foi possível excluir. {e}.")
        # Gravar arquivo JSON (Feito)
        case "5":
            # exibe os usuários cadastrados
            arquivo = input("Informe o nome do arquivo: ").strip()
            with open(f"atv01/{arquivo}.json","w",encoding="utf-8") as f:
                json.dump(usuarios, f)
            os.system("cls" if os.name == "nt" else "clear")
            print("Arquivo .json gravado com sucesso!")
            continue
        # Abrir novo arquivo JSON (Feito)
        case "6":
            try:
                arquivo = input("Informe o nome do .txt que deseja abrir: ").strip()
                with open(f"atv01/{arquivo}.json","r",encoding="utf-8") as f:
                    usuarios = json.load(f)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Dados importados com sucesso.")
            except Exception as e:
                print(f"Não foi possível abrir o arquivo. {e}.")
            # exibe o arquivo na tela

            continue
        # Sair do programa (Feito)
        case "7":
            break
        case _:
            print("Opção inválida.")
            continue