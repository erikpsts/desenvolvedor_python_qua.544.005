# and = e 
# or = ou
# nor = não

# Seu algorítmo depende de uma condicional? M ais de uma condicional?

nome = input("Informe seu nome: ").strip().title()
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura em metros: ").replace(",","."))

# verifique se o pagante possui os requisitos
if idade >= 12 and altura >= 1.35:
    print(f"{nome} está autorizado a entrar. ")
else:
    print(f"{nome} não está autorizado a entrar. ")