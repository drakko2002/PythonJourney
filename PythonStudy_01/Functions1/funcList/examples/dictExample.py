dicionarioTeste = {"ex1": 1, "ex2": 2, "ex3": 3}

#Objetivo do programa: Criar dicionário com 3 chaves
#Permitir que o usuário adicione, remova e visualize as chaves no fluxo principal
#Ao realizar uma dessas operações, ele deverá retornar um dicionário atualizado.
def modificar_chave(dicionario, chave, valor):
    print("Selecionou atualizar chave.")
    dicionario.update({chave: valor})
    print(f"Chave '{chave}' atualizada com valor '{valor}'.")
    return dicionario
#Bloco try/except retirado para reduzir redundância.



def excluir_chave(dicionario, chave):
    print("Selecionou excluir chave.")
    if chave in dicionario:
        dicionario.pop(chave)
        print(f"Chave '{chave}' foi removida.")
    else:
        print(f"A chave {chave} requisitada não existe.")


def visualizar_chave(dicionario, chave):
    print("Selecionou visualizar chave.")
    if chave in dicionario:
        print(f"Visualizando chave requisitada: {dicionario[chave]}")
    else:
        print(f"A chave {chave} não foi encontrada.")



def funcao_saida():
    print("Saindo do programa...")
    raise SystemExit("Fluxo do programa foi finalizado.")

def valida_opcao():
    while True:
        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao not in [1,2,3,4]:
                print("Suas opções são 1, 2, 3 e 4.")
                continue



            if opcao == 1:
                chave = input("Digite a chave: ")
                valor = int(input("Digite o valor da chave: "))
                modificar_chave(dicionarioTeste, chave, valor)


            #No fluxo secundário do programa
            #Temos as funções que invocam valores para
            #serem inseridos dentro do dicionário
            if opcao == 2:
                chave = input("Digite a chave que deseja excluir: ")
                excluir_chave(dicionarioTeste, chave)



            if opcao == 3:
                chave = input("Digite a chave que deseja visualizar: ")
                visualizar_chave(dicionarioTeste, chave)
                #Os valores requisitados ao usuário devem ser inseridos
                #Para então a função seja chamada e substitua ou adicione esses valores
                #Dentro do dicionário.


            if opcao == 4:
                funcao_saida()
                break


        except ValueError:
            print("O valor digitado está incorreto. Tente novamente.")
            continue
        except KeyboardInterrupt:
            print("Programa finalizado pelo usuário.")
            break
        except IndexError:
            print("Valor inesperado foi inserido. Tente novamente.")
            continue
        except KeyError:
            print("Um erro ocorreu ao realizar a ação desejada. Tente novamente.")
            continue


def fluxo():

    while True:
            try:
                print("Bem vindo ao fluxo principal do programa.")
                print("1 - Atualizar chave")
                print("2 - Excluir chave")
                print("3 - Visualizar chave")
                print("4 - Sair")
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

fluxo()
#A representação de dicionários em Python sugere que cada nome de chave esteja associado
#com um valor. Isto é, se a chave for apagado, o valor a ela associado também
#Será apagado, consequentemente.