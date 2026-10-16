# O usuário deverá escolher a sala do filme desejado. Se tiver a idade mínima, o programa imprime o ingresso e encerra. Senão, o programa impede a entrada do usuário e retorna a lista para que o mesmo possa escolher outro filme.

# 5 Salas de filme.
# Idade mínima de 16 anos.
# Se for maior que 16 anos, o igresso imprime e finaliza.
# Se não, o programa não imprime o ingresso e retorna pra lista de salas de filmes.
import os
os.system('cls')

nome = input("Informe seu nome: ").strip().title()
idade = input("Informe seu idade: ").strip().lower()

os.system('cls')

while True:
    print(f"{'-'*20} FILMES EM CARTAZ - KINOPLEX {'-'*20}")
    print("1 - Obsession [18+]")
    print("2 - A empregada [16+]")
    print("3 - Dentro da Baleia [14+]")
    print("4 - Zootopia [12+]")
    print("5 - Minions 3 [L]")

    try:
        filme = int(input("Digite o número que representa o filme desejado: "))
        match filme: 
            case 1: 
                if idade >= 18:
                    print("Bom filme! Apresente o ingresso na sala 01. ")
                else:
                    print("Idade fora da faixa recomendada.")
            case 2:
                if idade >= 16:
                    print("Bom filme! Apresente o ingresso na sala 02.")
                else: 
                    print("Idade fora da faixa recomendada.")
            case 3:
                if idade >= 14:
                    print("Bom filme! Apresente o ingresso na sala 03.")
                else:
                    print("Idade fora da faixa recomendada.")
            case 4:
                if idade >= 12:
                    print("Bom filme! Apresente o ingresso na sala 04.")
                else:
                    print("Idade fora da faixa recomendada.")
            case 5:
                if idade >= 0:
                    print("Bom filme! Apresente o ingresso na sala 5.")
                else:
                    print("Idade fora da faixa recomendada.")
            case _:
                print("O filme não está no catálogo.")
        pergunta = (input("Digite 'sim' para escolher o filme novamente e qualquer outra coisa para encerrar. "))

        if pergunta == 'sim':
            os.system('cls')
            continue
        else:
            break
    except Exception as e:
        print(f"Deu erro {e}.")