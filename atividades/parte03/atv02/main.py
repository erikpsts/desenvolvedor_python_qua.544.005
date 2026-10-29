# TODO: parte 03 atividade 02
'''
Crie um programa em que o usuário informe um número inteiro e o programa retorne a sequência Fibonacci.
'''
# Solicita um número inteiro ao usuário

n = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))

# Inicializa os dois primeiros termos
t1 = 0
t2 = 1

# Contador de termos exibidos
contador = 0

if n <= 0:
    print("Por favor, digite um número inteiro maior que zero.")
elif n == 1:
    print(f"Sequência de Fibonacci: {t1}")
else:
    print("Sequência de Fibonacci:", end=" ")
    while contador < n:
        print(t1, end=" " if contador < n - 1 else "\n")
        proximo = t1 + t2
        t1 = t2
        t2 = proximo
        contador += 1
