def divide():
    try:
        a = float(input("Digite o numerador: "))
        b = float(input("Digite o denominador: "))
        division = a / b
        print(division)

    except ZeroDivisionError as error:
        print(error)
        print("Impossível dividir por zero.")


    except ValueError as error:
        print(error)
        print("Digite um valor válido.")


    except KeyboardInterrupt as error:
        print(error)
        raise SystemExit(f"Usuário optou por finalizar programa. {error}")


divide() #Chama pela função divide.