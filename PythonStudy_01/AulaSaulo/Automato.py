def alphabet():
    palavra = input("Digite algo: ")
    try:
        if palavra == '00' or '00' in palavra:
            print("Palavra aceita!")
        else:
            print("Palavra recusada.")
    except TypeError as e1:
        print("Entrada inválida.")
    except ValueError as e2:
        print("Tipo inválido.")

alphabet()