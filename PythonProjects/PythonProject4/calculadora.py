#Projeto de calculadora base
from soma import funcsoma
from subtrai import funcsub

def calculadora():
    while True:
        print("\n--- Calculadora Simples para testes ---")
        print("Escolha uma operação matemática!")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Sair")

        try:
            opcao = int(input("Digite o número da opção desejada: "))
            if opcao not in [1, 2, 3]:
                print("Opção inválida! Digite algo entre 1 e 3.")
                continue



            if opcao == 1:
                funcsoma()

            elif opcao == 2:
                funcsub()

            elif opcao == 3:
                print("Encerrando calculadora!")
                break
        except ValueError:
            print("Opção inválida! Digite apenas números.")




calculadora()