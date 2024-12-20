def funcsoma():
    try:
        first = float(input("Digite o primeiro número: "))
        second = float(input("Digite o segundo número: "))

        soma = first + second

        print(f"A soma de {first} e {second} é igual a: {soma}")

    except ValueError:
        print("Digite valores válidos.")