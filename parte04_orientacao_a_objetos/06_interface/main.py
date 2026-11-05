# Bibliotecas
import os
import random

from model import Conta


def limpar():
    os.system("cls" if os.name == "nt" else "clear") 

def main():
    # Instância a classe Conta
    cc = Conta(
        titular="",
        cpf="",
        agencia="1010-1",
        n_conta=f"{random.randint(10000,99999)}-1",
        saldo=0.0
        )

    # TODO: terminar amanhã


if __name__ == "__main__":
    main()
