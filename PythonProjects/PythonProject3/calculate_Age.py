from time_func import timeFunction

def calculate():
    while True:
        try:
            birth_year = int(input("What's the birthyear: ")) #Converte a input do usuário para inteiro.
        except ValueError:
            print("Digite apenas números inteiros.")
            continue

        actual_year = timeFunction()

        calc_Age = int(actual_year) - int(birth_year)



        print("A idade do individuo é: ", calc_Age)
        print(f"\nFim do programa.\n")
        break
calculate()