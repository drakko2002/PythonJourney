from carroPy import Carro
from carroPy import carro1
from carroPy import carro2

while True:
    print(f"--//--Bem vindo ao menu de testes para classe carro!--//--")
    print(f"Digite 1 para obter as informações do carro Honda.")
    print(f"Digite 2 para obter as informações do carro Hilux.")
    print(f"Digite 3 para encerrar o programa.")

    try:
        opcao = int(input("\nDigite a opção desejada: "))
        if opcao not in [1, 2, 3]:
            print("Suas opções são apenas 1, 2 e 3.")
            continue

        if opcao == 1:
            print(carro1())

        if opcao == 2:
            print(carro2())

        if opcao == 3:
            print("Saindo do programa...")
            break
    except ValueError:
        print("Digite um número correspondente ao menu!")
        continue