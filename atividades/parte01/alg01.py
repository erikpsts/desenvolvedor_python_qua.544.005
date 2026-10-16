# TODO: Atividade 01
'''
Crie um programa que receba o nome, a massa em kg e a altura em metros do usuário, calcule seu IMC (indice de massa corporal) e finalize informando o diagnóstico do usuário com base no valor do IMC (se está abaixo do peso, sobrepeso, no peso ideal...)
'''
nome = str(input("Digite o seu nome: ")).strip().title()
massa = float(input("Digite seu peso: "))
altura = float(input("Digite a sua altura "))

imc = massa / (altura ** 2)
try:
    if imc <= 18.5:
        print(f"Abaixo do peso. IMC de: {imc}")
    elif imc >= 18.5 and imc < 29.4:
        print(f"Peso ideal. IMC de: {imc}")
    elif imc >= 25.0 and imc < 29.9:
        print(f"Sobrepeso. IMC de: {imc}")
    elif imc >= 29.9 and imc < 34.9:
        print(f"Obesidade grau 1. IMC de: {imc}")
    elif imc >= 34.9 and imc < 45:
        print(f"Obesidade grau 2. IMC de: {imc}")
    else:
        print(f"Obesidade grau 3. IMC de: {imc}")

except Exception as e:
        print(f"Deu erro! {e}")