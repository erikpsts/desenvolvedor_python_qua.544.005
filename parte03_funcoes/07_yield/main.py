from modulo import eq_2o_grau,limpar

def main():
    print("Cálculo da equação do segundo grau")
    a = float(input("Informe o valor de 'a': ").replace(",","."))
    b = float(input("Informe o valor de 'b': ").replace(",","."))
    c = float(input("Informe o valor de 'c': ").replace(",","."))
    limpar()

    if a != 0:
        result = eq_2o_grau(a,b,c)
        print("Resultado da equação do segundo grau: ")
        for x in result:
            print(f"x = {x}")
    else:
        print("Os valores não são de equação do 2° grau")

if __name__ == "__main__":
    main()