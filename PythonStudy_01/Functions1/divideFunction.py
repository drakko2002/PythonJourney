def divide():
    try:
        a = float(input("Digite o numerador: ")) #Pede para usuário inserir dados A.
        b = float(input("Digite o denominador: ")) #Pede para usuário inserir dados B.
        division = a / b #Tenta realizar operação de divisão com A e B fornecidos.
        print(division) #Imprime o resultado da Divisão na tela, se for bem-sucedida.

    except ZeroDivisionError as error: #Chama pela exceção ZeroDivision da classe Error,
        print(error) #Imprime detalhes do erro.
        print("Impossível dividir por zero.")


    except ValueError as error: #Chama pela exceção ValueError da classe Error.
        print(error) #Imprime detalhes do erro.
        print("Digite um valor válido.")


    except KeyboardInterrupt as error: #Chama pela Exceção KeyboardInterrupt.
        print(error)
        raise SystemExit(f"Usuário optou por finalizar programa. {error}") from error


divide() #Chama pela função divide.