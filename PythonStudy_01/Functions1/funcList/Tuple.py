'''Cálculo com tuplas

Crie uma tupla com 5 números inteiros.
Calcule e exiba:
- A soma de todos os elementos.
- O maior e o menor valor.
- A posição do maior número na tupla.'''
numbers: tuple = (1, 2, 3, 4, 5)
#I decided to typecast the tuple.
def sum_tuple(numbers: tuple) -> int: #Indica que o retorno esperado é INT
    return sum(numbers)
def max_tuple(numbers: tuple) -> int:
    #Typecasting the numbers for tuple again, as return value points to int.
    return max(numbers)
#The sum function returns the sum of a __start__ value provided by the function.
def min_tuple(numbers: tuple) -> int:
    return min(numbers)
def position_tuple(numbers: tuple) -> int:
    return numbers.index(max(numbers))
    #Retorna o maior elemento dentro da tupla.
    #The .index function as a object-like method from the tuple form allows us to
#Print the highest element of the tuple without further difficulties.
def highest_tuple(numbers: tuple) -> int:
    return numbers[numbers.index(max(numbers))]

def main():
    while True:
        print("-->Bem vindo ao Menu de Teste da Tupla <--")
        print("1 - Somar Tupla")
        print("2 - Quantidade de elementos da tupla.")
        print("3 - Menor valor da tupla, apenas.")
        print("4 - Maior valor da tupla, apenas.")
        print("5 - Posição do maior valor da tupla.")
        print("6 - Quantidade de elementos da tupla.")
        print("7 - Sair")
        try:
            opcao_menu = int(input("Digite a opção desejada: "))
            if opcao_menu == 1:
                #sum_tuple(numbers)
                print(sum_tuple(numbers))

                break

            elif opcao_menu == 2:
                print(highest_tuple(numbers))
                break


            elif opcao_menu == 3:
                print(min_tuple(numbers))
                break


            elif opcao_menu == 4:
                print(max_tuple(numbers))
                break


            elif opcao_menu == 5:
                print(position_tuple(numbers))
                break


            elif opcao_menu == 6:
                print(f"Tupla tem {len(numbers)} elementos.")
                #A única razão pra isso funcionar, é a função print que executa algo independente.
                break

                
            elif opcao_menu == 7:
                raise SystemExit("Programa encerrado.")


        except (ValueError):
            print("Digite uma opção válida.")
            continue
        except (KeyboardInterrupt):
            print("Programa encerrado.")
            break
#Cant forget to call the main() function to start the flux of the program.
main()