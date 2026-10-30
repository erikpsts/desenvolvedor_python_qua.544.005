import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

    def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

def main():
    limpar()
    n = int(input("Informe o número de sequências Fibonacci: "))
    print(fibonacci(n))