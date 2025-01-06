'''Cálculo com tuplas

Crie uma tupla com 5 números inteiros.
Calcule e exiba:
- A soma de todos os elementos.
- O maior e o menor valor.
- A posição do maior número na tupla.'''
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

def add_tuple(numbers: tuple) -> tuple:
    num = int(input("Digite elemento para adicionar"))
    return numbers + (num,)

def del_tuple(numbers: tuple) -> tuple:
    return numbers[:-1]

def view_tuple(numbers: tuple) -> tuple:
    return numbers


def main():
    numbers: tuple = (1, 2, 3, 4, 5)
    while True:
        print("-->Bem vindo ao Menu de Teste da Tupla <--")
        print("1 - Somar Tupla")
        print("2 - Quantidade de elementos da tupla.")
        print("3 - Menor valor da tupla, apenas.")
        print("4 - Maior valor da tupla, apenas.")
        print("5 - Posição do maior valor da tupla.")
        print("6 - Quantidade de elementos da tupla.")
        print("7 - Adicionar elemento a tupla.")
        print("8 - Remover elemento a tupla.")
        print("9 - Ver elementos da tupla.")
        print("10 - Sair")
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
                numbers = add_tuple(numbers)
                print(f"Tupla atualizada: {numbers}")




            elif opcao_menu == 8:
                numbers = del_tuple(numbers)
                print(f"Tupla atualizada: {numbers}")

            elif opcao_menu == 9:
                print(view_tuple(numbers))

            elif opcao_menu == 10:
                raise SystemExit("Programa encerrado.")


        except (ValueError, TypeError):
            print("Digite um valor válido.")
            continue
        except (KeyboardInterrupt):
            print("Programa encerrado.")
            break
#Cant forget to call the main() function to start the flux of the program.
main()
#Due to Tuples inate imutability, it's imposible to direct add a element and delete a element
#From it. Althought we can still create another tuple which can replace the current tuple
#elements.
####################
#Also, by re-declaring the tuple with the respective function willing to modify it's elements
#It will also update the tuple with the inserted values.