# Bibliotecas
import os 

# Lista
nomes = ["Alex", "Charlotte", "Scarley", "John", "Jinx", "Jason", "Michael", "Connor"]

os.system("cls" if os.name == "nt" else "clear")

# Loop
while True:
    # Exibe a lista original
    for n, nome in enumerate(nomes):
        print(f"Índice {n}: {nome}")
    
    # Menu
    print("1 - Alternar item da lista")
    print("2 - Finalizar")
    opcao = input("Opção desejada: ").strip() # Informe a opção desejada

    # Verifica a opção escolhia
    match opcao:
        case "1":
            # Informa índice a ser alterado
            indice = int(input("Informe o índice a ser alterado: "))
            # Informa novo valor
            nomes[indice] = input("Informe novo nome: ").strip().title()
            os.system("cls" if os.name == "nt" else "clear")
            print("Item da lista alterado com sucesso!")
            continue 
        case "2":
            os.system("cls" if os.name == "nt" else "clear")
            # Exibe a nova lista
            for n, nome in enumerate(nomes):
                print(f"Índice {n}: {nome}")
            break
        case _:
            print("Opção inválida")
            continue