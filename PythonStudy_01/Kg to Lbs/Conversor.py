from Weight import weight
from Kilogram import kilogram
from Pounds import pounds

def conversor():
    while True:
        print("\n--Bem vindo ao conversor de peso!--")
        print("Digite 1 para converter de Kg para Libras.")
        print("Digite 2 para converter de Libras para Kg.")
        print("Digite 3 para encerrar o programa.")

        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao not in [1,2,3]:
                print("Digite uma opção válida.")
                continue

            if opcao == 1:
                pounds()

            elif opcao == 2:
                kilogram()



            if opcao == 3:
                print("Até nunca mais, Thais Carla!")
                break
        except ValueError:
            print("Puta merda.")

conversor()
