nome = str(input("Digite o seu nome: ")).strip().title()
massa = float(input("Digite seu peso: ").replace(",", "."))
altura = float(input("Digite a sua altura: ").replace(",", "."))

# Calcula o imc do usuário
imc = massa/(altura**2)

# Exibe o valor do IMC com duas casas decimais
print(f"Olá {nome}, seu IMC é: {imc:.2f}!")

if imc < 18.5:
    print(f"Abaixo da massa.")
elif imc < 25.0:
    print(f"Massa ideal.")
elif imc < 30.0:
    print(f"Você está com a massa acima do normal.")
elif imc < 35.0:
    print(f"Obesidade grau 1.")
elif imc < 40.0:
    print(f"Obesidade grau 2.")
else:
    print(f"Obesidade grau 3.")