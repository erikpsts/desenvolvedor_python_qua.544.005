#biblioteca
import os

#funções
def limpar():
    os.system("cls" if os.name == "nt" else "clear")
#o return e o comando final de uma função
def boas_vindas(nome):
    return f"{nome},seja bem vindo!"

#algoritmo principal
limpar()
nome = input("Informe seu nome: ").strip().title()
print(boas_vindas(nome))