def soma():
    a = int(input("Digite um valor: "))
    b = int(input("Digite outro valor: "))
    soma: int = a + b
    print(">>> Soma: ", soma.__float__())


def division():
    a = float(input("Digite um valor: "))
    b = float(input("Digite um valor diferente de zero: "))
    divide: float = a/b
    print(">>>Divide: ", divide)


def sub():
    a = int(input("Digite um valor: "))
    b = int(input("Digite outro valor: "))
    sub: int = a - b
    print(">>>Sub: ", sub)


def final():
    print("Fim do programa.")
    raise KeyboardInterrupt


while True:
    print("Bem vindo à calculadora de testes!")
    print("1 - Soma")
    print("2 - Divide")
    print("3 - Subtrai")
    print("4 - Sair")
    try:
        option = int(input("Digite a opção desejada: "))
        print(option)


        if option not in [1,2,3,4]:
            print("Digite uma opção válida.")
            continue


        if option == 1:
            print("Selecionado operação Soma.")
            soma()


        elif option == 2:
            print("Selecionado operação Divide.")
            division()


        elif option == 3:
            print("Selecionado operação Subtrai.")
            sub()


        elif option == 4:
            print("Escolheu sair do programa.")
            break


    except (ValueError, ZeroDivisionError) as e:
        print("Digite um valor válido!")
        continue
    except KeyboardInterrupt:
        print("Programa encerrado pelo usuário.")
#    finally: #Independente das exceções serem tratadas ou não, o bloco finally finaliza o programa.
        break
        #break #Se colocar continue nisso, impede o usuário de interromper programa.


#Um bloco finally sugere uma expressão de código que será executada como prioridade
#Não importando se expressões anteriores foram executadas ou não.
