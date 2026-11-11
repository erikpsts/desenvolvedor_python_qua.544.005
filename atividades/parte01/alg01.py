# atividade 01
'''
Crie um programa que receba o nome, a massa em kg e a altura em metros do usuário, calcule seu IMC (índice de massa corporal) e finalize informado o diagnóstico do usuário com base no valor do IMC (se está magro, gordo, no peso ideal...)
'''
# entrada de dados
nome = str(input("Digite o seu nome: ")).strip().title()
massa = float(input("Digite sua massa em kg: ").replace(",", "."))
altura = float(input("Digite a sua altura em metros: ").replace(",", "."))

# Calcula o imc do usuário
imc = massa/(altura**2)

# Exibe o valor do IMC com duas casas decimais
print(f"Olá {nome}, seu IMC é: {imc:.2f}!")

# Informa o diagnóstico do usuário com base no valor do IMC
if imc < 18.5:
    print(f"Você está com massa abaixo do normal.")
elif imc < 25.0:
    print(f"Você está com massa normal.")
elif imc < 30.0:
    print(f"Você está com massa acima do normal.")
elif imc < 35.0:
    print(f"Você está obeso.")
elif imc < 40.0:
    print(f"Você está com obesidade nível II.")
else:
    print(f"Você est]á com obesidade mórbida.")

