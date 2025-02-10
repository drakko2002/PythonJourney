def check_number():
    try:
        while True:
            x = int(input("Digite o número: "))
            match x:
                case 10:
                    print("O número digitado é 10.")
                case 20:
                    print("O número digitado é 20.")
                case 0 :
                    print("O número digitado é menor que 100.")
            if not x:
                check_number()
            if x:
                break
    except ValueError:
        print("Entrada inválida.")
        return check_number()

check_number()
