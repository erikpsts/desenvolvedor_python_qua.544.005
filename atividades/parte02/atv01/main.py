# TODO: parte 02 atividade 01
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

while True:
    # menu 
    print("1 - Cadastrar novo usuário") # Feito
    print("2 - Listar usuários") # Feito
    print("3 - Alterar dados de um usuário") #TODO
    print("4 - Excluir um usuário") # TODO
    print("5 - Gravar arquivo JSON") # Feito
    print("6 - Abrir arquivo JSON") # Feiro
    print("7 - Sair do programa") # Feito
    opcao = input("Opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        # (cadastra novo usuário) (Feito)
        case "1":
            # novo dicionário
            usuario = {}
           
            # insere os dados do usuário
            usuario['nome'] = input("Informe o nome: ").strip().title()
            usuario['email'] = input("Informe o e-mail: ").strip().lower()
            usuario['telefone'] = input("Informe o telefone: ").strip()
            usuario['cpf'] = input("Informe o CPF: ").strip()
           
            # adiciona usuário na lista
            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")
           
            # mensagem de confirmação
            print(f"{usuario.get('nome')} cadastro com sucesso!")
            continue
        # Listar usuários (Feito)
        case "2":
            # exibe os usuários cadastrados
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                print(f"{'-'*40}")
            # pergunta ao usuário se deseja prosseguir
            prosseguir = input("Deseja continuar cadastrando novo usuário? (sim/não)").strip().lower()
            if prosseguir == "sim":
                os.system("cls" if os.name == "nt" else "clear")
                # novo dicionário
                usuario = {}
                
                # insere os dados do usuário
                usuario['nome'] = input("Informe o nome: ").strip().title()
                usuario['email'] = input("Informe o e-mail: ").strip().lower()
                usuario['telefone'] = input("Informe o telefone: ").strip()
                usuario['cpf'] = input("Informe o CPF: ").strip()
                
                # adiciona usuário na lista
                usuarios.append(usuario)
                os.system("cls" if os.name == "nt" else "clear")
                
                # mensagem de confirmação
                print(f"{usuario.get('nome')} cadastro com sucesso!")
                continue
            else:
                os.system("cls" if os.name == "nt" else "clear")
                break
        # Alterar dados de um usuário ( TODO )
        case "3":
            os.system("cls" if os.name == "nt" else "clear")
            try:
               # TODO
               pass
            except Exception as e:
                print(f"Não foi possível abrir o arquivo. {e}.")
            continue
        # Excluir um usuário ( TODO )
        case "4":
            del usuarios 
            # TODO
            pass
        # Gravar arquivo JSON (Feito)
        case "5":
            # exibe os usuários cadastrados
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                print(f"{'-'*40}")
            # pergunta ao usuário se deseja prosseguir
            prosseguir = input("Deseja gravar os dados? (s/n)").strip().lower()
            if prosseguir == "s":
                os.system("cls" if os.name == "nt" else "clear")
                arquivo = input("Informe o nome do arquivo: ").strip()
                with open(f"16_JSON/{arquivo}.json","w",encoding="utf-8") as f:
                    json.dump(usuarios, f)
                print("Arquivo json gravado com sucesso!")
                continue
            else:
                os.system("cls" if os.name == "nt" else "clear")
                continue
        # Abrir novo arquivo JSON (Feito)
        case "6":
            os.system("cls" if os.name == "nt" else "clear")
            abrir_arquivo = input("Informe o nome do .txt que deseja abrir: ").strip()
            with open(f"atv01/{abrir_arquivo}.txt","r",encoding="utf-8") as f:
                texto = f.read()
            # exibe o arquivo na tela
            print(texto)
            continue
        # Sair do programa (Feito)
        case "7":
            break
        case _:
            print("Opção inválida.")
            continue
