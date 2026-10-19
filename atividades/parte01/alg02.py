# O cliente não deseja saber como foi feito. Apenas se foi feito.
# Import a biblioteca os para limpar a tela do terminal
import os

# Limpa a tela do terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Dados do usuário
nome = input("Informe seu nome: ").strip().title()
idade = int(input("Informe sua idade: ").strip())
idade_minima = None

os.system('cls')

# loop para exibir o menu de filmes e verificar a idade do usuário
while True:
    # menu de filmes
    print(f"{'-'*20} FILMES EM CARTAZ - KINOPLEX {'-'*20}")
    print("Sala 1 - Obsession [18+]")
    print("Sala 2 - A empregada [16+]")
    print("Sala 3 - Dentro da Baleia [14+]")
    print("Sala 4 - Zootopia [12+]")
    print("Sala 5 - Minions 3 [L]")

    # Sala desejada pelo usuário
    sala = input("Digite o número da sala desejada: ").strip()

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
            print("O filme não está no catálogo.")
            idade_minima = idade + 1
    # Verifica a idade do usuário e imprime o ingresso se ele for maior ou igual a idade mínima
    if idade >= idade_minima:
        print(f"Ingresso impresso para {nome}.")  
        print("Tenha um bom filme!")  
        break
    else:
        print(f"Ingresso negado para {nome}.")
        print(f"Você não atende aos requisitos de idade para este filme.")
        print(f"Por favor, escolha outro filme: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        continue 