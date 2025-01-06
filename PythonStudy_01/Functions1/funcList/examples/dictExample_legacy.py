dicionarioTeste = {"ex1": 1, "ex2": 2, "ex3": 3}

#Objetivo do programa: Criar dicionário com 3 chaves
#Permitir que o usuário adicione, remova e visualize as chaves no fluxo principal
#Ao realizar uma dessas operações, ele deverá retornar um dicionário atualizado.

#O código a seguir falhou em seu funcionamento e teve de ser refatorado.
#Ainda sim, será mantido um registro para estudos futuros.

#As funções possuem blocos de try/except que induzem loopings infinitos e confusos.

#E pelas variáveis terem sido declaradas globalmente, a utilidade era porca.

def valida_opcao():
    while True:
        try:
            opcao = int(input("Digite opção desejada: "))
            if opcao not in [1,2,3,4]:
                print("Suas opções são 1, 2, 3 e 4.")
                continue
            if opcao == 1:
                print("Selecionou atualizar chave.")
                try:
                    acao_chave = input("Digite a chave: ")
                    valor_chave = int(input("Digite o valor da chave: "))

                    print("Chave atualizada!")

                    dicionarioTeste.update({acao_chave: valor_chave})
                    print(dicionarioTeste)
                except(KeyError,IndexError,ValueError) as error:
                    print(error)
                    print("Algo aconteceu. Tente novamente.")
                    continue
            if opcao == 2:
                acao_chave = input("Digite a chave que deseja excluir: ")
                print("Selecionou excluir chave.")
                print(acao_chave)

                if acao_chave in dicionarioTeste:
                    dicionarioTeste.pop(acao_chave)
                    print(dicionarioTeste)
                    return
                #Retorna versão atualizada do dicionário.
                else:
                    raise ValueError("Chave não existe.")

            if opcao == 3:
                print("Selecionou visualizar chave.")
                acao_chave = input("Digite a chave que deseja visualizar: ")
                print(acao_chave)
                if acao_chave in dicionarioTeste:
                    print(dicionarioTeste[acao_chave])
                    return dicionarioTeste
                #retorna versão atualizada do dicionário
                if acao_chave not in dicionarioTeste:
                    print("A chave não existe.")
                    continue
            if opcao == 4:
                print("Saindo do programa...")
                raise SystemExit("Fluxo do programa foi finalizado.")

            #Sessão de tratamento de erros.
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
            print("--> Menu do Dicionário <--")
            print("1 - Modificar chave")
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