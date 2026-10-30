import os 

from model import Pessoa

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    limpar()

    usuario = Pessoa(nome="",idade=0,email="")

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.idade = int(input("Informe o nome: "))
    usuario.email = input("Informe o nome: ").strip().lower()

    print(usuario.cumprimentar())

if __name__ == "__main__":
    main()
    