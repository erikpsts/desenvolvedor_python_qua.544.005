# atividade 02
'''
Crie um programa em que o usuário informe uma única vez o nome e a idade, e em seguida, o programa exibe uma lista de 5 filmes do cinema e suas respectivas salas e classificações indicativas.
O usuário deverá escolher a sala do filme desejado. Se tiver a idade mínima, o programa imprime o ingresso e encerra. Senão, o programa impede a entrada do usuário e retorna a lista para que o mesmo possa escolher outro filme.
'''
import os

# Limpa a tela do terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Dados do usuário
nome = input("Informe seu nome: ").strip().title()
idade = int(input("Informe sua idade: ").strip())
idade_minima = None

# loop 
while True:
    # menu de filmes
    print(f"{'-'*20} FILMES EM CARTAZ - KINOPLEX {'-'*20}")
    print("Sala 1 - Obsession [18+]")
    print("Sala 2 - A empregada [16+]")
    print("Sala 3 - Dentro da Baleia [14+]")
    print("Sala 4 - Zootopia [12+]")
    print("Sala 5 - Minions 3 [L]")

    # Sala desejada pelo usuário
    sala = input("Sala desejada: ").strip()

    # atribui a idade mínima do filme
    match sala: 
        case "1": 
            idade_minima = 18
        case "2":
            idade_minima = 16
        case "3":
            idade_minima = 14
        case "4":
            idade_minima = 12
        case "5":
            idade_minima = 0
        case _:
            print("Sala inexistente.")
            idade_minima = idade + 1
    # Verifica a idade do usuário
    if idade >= idade_minima:
        print(f"Ingresso impresso para {nome}.")  
        print("Tenha um bom filme!")  
        break
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Ingresso negado para {nome}.")
        print(f"Você não atende aos requisitos de idade para este filme.")
        print(f"Por favor, escolha outro filme: ")
        continue 