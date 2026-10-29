def main(): 
    # menu
    print(f"{'-'*20} Índice {'-'*20}")
    print("Escolha o planeta que deseja calcular seu peso:")
    print("1 - Mercúrio")
    print("2 - Vênus")
    print("3 - Terra")
    print("4 - Marte")
    print("5 - Júpiter")
    print("6 - Saturno")
    print("7 - Urano")
    print("8 - Netuno")
    print("9 - Lua")
    print("10 - Sair do programa")

    planetas = input("Operação desejada: ").strip()
    massa = float(input("Digite sua massa em KG:").strip())

    # escolha
    match planetas:
        # Mercúrio
        case "1":
            gravidade = 3.75
            peso = massa*gravidade
            print(f"Seu peso em Mercúrio é {peso}N.")
        # Vênus
        case "2":
            gravidade = 8.87
            peso = massa*gravidade
            print(f"Seu peso em Vênus é {peso}N.")
        # Terra
        case "3":
            gravidade = 9.80
            peso = massa*gravidade
            print(f"Seu peso na Terra é {peso}N.")
        # Marte
        case "4":
            gravidade = 3.71
            peso = massa*gravidade
            print(f"Seu peso em Marte é {peso}N.")
        # Júpiter
        case "5":
            gravidade = 24.79
            peso = massa*gravidade
            print(f"Seu peso em Júpiter é {peso}N.")
        # Saturno
        case "6":
            gravidade = 10.44
            peso = massa*gravidade
            print(f"Seu peso em Saturno é {peso}N.")
        # Urano
        case "7":
            gravidade = 8.87
            peso = massa*gravidade
            print(f"Seu peso em Urano é {peso}N.")
        # Netuno
        case "8":
            gravidade = 11.15
            peso = massa*gravidade
            print(f"Seu peso em Netuno é {peso}N.")
        # Lua
        case "9":
            gravidade = 1.6
            peso = massa*gravidade
            print(f"Seu peso na Lua é {peso}N.")
            
        #NOTE: SIX SEVEN
        case _: 
            print("Operação inválida.")

if __name__ == "__main__":
    main()