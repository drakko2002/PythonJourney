'''def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9'''

celsius_to_fahrenheit = lambda celsius: (celsius * 9/5) + 32
fahrenheit_to_celsius = lambda fahrenheit: (fahrenheit - 32) * 5/9

def main():
    while True:
        print("--> Conversor de temperatura <--")
        print("Digite F para Fahrenheit ou C para Celsius: ")
        print("Para sair digite 'sair' ou 'Sair'")
        try:
            opcao = input("Digite a opção desejada: \n")

            if opcao == "F":
                heit = float(input("Digite a temperatura em Fahrenheit: "))
                result = fahrenheit_to_celsius(heit)
                print(result)
            elif opcao == "C":
                celsium = float(input("Digite a temperatura em Celsius: "))
                result = celsius_to_fahrenheit(celsium)
                print(result)
            elif opcao == "sair" or opcao == "Sair":
                raise SystemExit("Usuário escolheu sair do programa.")
        except ValueError:
            print("Erro no valor inserido.")
            continue
        except KeyboardInterrupt:
            raise SystemExit("Programa encerrado pelo usuário.")
if __name__ == "__main__":
    main()
#O inicializador de Main necessita dois sinais de igual/assignment.