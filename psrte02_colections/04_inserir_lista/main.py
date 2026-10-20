import os # Biblioteca


tarefas = [] # To do list;


os.system("cls" if os.name == "nt" else "clear") # Limpar o terminal;


while True: # Loop
    # Menu
    print("1 - Inserir nova tarefa na lista")
    print("2 - Finalizar o exibir lista")
    opcao = input("Opção desejada: ").strip() # Informe a opção desejada;

    match opcao:
        case "1":
            nova_tarefa = input("Informe a nova tarefa: ")  # Usuário informa novo item na lista;
            tarefas.append(nova_tarefa) # Insere o item escrito pelo usuário na lista;
            continue # Retorna para o início do loop;
        case "2":
            os.system("cls" if os.name == "nt" else "clear")

            # Exibe a lista;
            for n, tarefa in enumerate(tarefas, start=1):
                print(f"{n}° tarefa: {tarefa}")
            break # Encerra o loop
        case _:
            print("Opção inválida.")