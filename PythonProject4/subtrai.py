def funcsub():
    try:
        first_num = float(input("Digite primeiro elemento: "))
        second_num = float(input("Digite segundo elemento: "))

        subtrai = first_num - second_num

        print(f"O resultado da subtração de {first_num} com {second_num} é {subtrai}")

    except ValueError:
        print("É impossível executar a operação com os valores digitados.")