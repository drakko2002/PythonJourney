# Python
def insert(num):
    num.append(int(input("\nEnter a number to insert at the end of the list: ")))
    print(f"\nA lista agora contém {num}")


def lista():
    numbers = [1, 2, 3, 4, 5]
    print(f"\nA lista agora contém {numbers}")

    while True:
        print(f"\nDeseja inserir mais itens na lista? [S/N]")
        resposta = input().strip().upper()
        if resposta == "N":
            print("\nFinalizando lista-numero.")
            break
        elif resposta == "S":
            insert(numbers)
        else:
            print("\nPor favor, digite 'S' para Sim ou 'N' para Não.")



lista()
