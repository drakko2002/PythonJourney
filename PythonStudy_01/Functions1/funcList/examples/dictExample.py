dicionarioTeste = {"ex1": 1, "ex2": 2, "ex3": 3}
print(dicionarioTeste)


#Objetivo do programa: Criar dicionário com 3 chaves
#Permitir que o usuário adicione, remova e visualize as chaves no fluxo principal
#Ao realizar uma dessas operações, ele deverá retornar um dicionário atualizado.


def valida_opcao():

    while valida_entrada not in:
        try:
            valida_entrada = int(input("Digite uma opção entre 1 e 5: "))
            print(valida_entrada)
            if valida_entrada not in opcao:
                raise ValueError
            if valida_entrada in opcao:
                break
        except ValueError:
            print("A opção inserida não existe.")
            valida_opcao()


valida_opcao()


def fluxo():
    while True:
        try:
            print("--> Menu do Dicionário <--")
            print("1 - Adicionar chave")
            print("2 - Modificar chave")
            print("3 - Excluir chave")
            print("4 - Visualizar chave")
            print("5 - Sair")
            valida_opcao()
        except ValueError:
            print("Opção inválida.")
            fluxo()
        except KeyboardInterrupt:
            print("Programa encerrado.")
            break
        except SystemExit:
            print("Programa encerrado.")
            break


'''        valida_chave = str(input("Digite uma chave: "))
        modifica_chave = int(input("Digite um valor: "))
        if valida_chave in dicionarioTeste:
            print("Deseja modificar a chave?")
            print("1 - Sim")
            print("2 - Não")
            print("2 - Sair")
'''
