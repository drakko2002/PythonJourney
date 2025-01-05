dicionarioTeste = {"ex1": 1, "ex2": 2, "ex3": 3}
print(dicionarioTeste)


def valida_opcao(opcao):
    opcao = [1, 2, 3, 4, 5]
    valida_entrada = int(input("Digite uma opção entre 1 e 5: "))
    while valida_entrada not in opcao:
        try:
            print(valida_entrada)
            if valida_entrada not in opcao:
                raise ValueError
        except ValueError:
            print("A opção inserida não existe.")
            valida_opcao(opcao)


def fluxo():
    while True:
        print("--> Menu do Dicionário <--")
        print("1 - Adicionar chave")
        print("2 - Modificar chave")
        print("3 - Excluir chave")
        print("4 - Visualizar chave")
        print("5 - Sair")

'''        valida_chave = str(input("Digite uma chave: "))
        modifica_chave = int(input("Digite um valor: "))
        if valida_chave in dicionarioTeste:
            print("Deseja modificar a chave?")
            print("1 - Sim")
            print("2 - Não")
            print("2 - Sair")
'''