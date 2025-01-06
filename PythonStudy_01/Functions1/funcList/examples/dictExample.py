dicionarioTeste = {"ex1": 1, "ex2": 2, "ex3": 3}
print(dicionarioTeste)


#Objetivo do programa: Criar dicionário com 3 chaves
#Permitir que o usuário adicione, remova e visualize as chaves no fluxo principal
#Ao realizar uma dessas operações, ele deverá retornar um dicionário atualizado.


def valida_opcao():
    while True:
        try:
            opcao = int(input("Digite a opção desejada: "))
            atualiza_chave = input("Digite a chave a ser atualizada: ")
            valor_chave = int(input("Digite o valor da chave: "))
            acao_chave = str(input("Digite a chave: "))
            if opcao not in [1,2,3,4,5]:
                print("Suas opções são 1, 2, 3, 4 e 5.")
                #Ao invocar Raise ValueError aqui, o código finaliza por erro de valor.
                #Isso torna o "continue" do bloco inalcançável.
                continue
            if opcao == 1:
                print("Selecionou atualizar chave.")
                print(atualiza_chave)
                print(valor_chave)
                print("Chave atualizada!")
                dicionarioTeste.update({atualiza_chave: valor_chave})
                print(dicionarioTeste)
            if opcao == 2:
                print("Selecionou excluir chave.")
                print(acao_chave)
                dicionarioTeste.pop(acao_chave)
            if opcao == 3:
                print("Selecionou visualizar chave.")
                print(acao_chave)
                if acao_chave in dicionarioTeste:
                    print(dicionarioTeste[acao_chave])
                    break
                if acao_chave not in dicionarioTeste:
                    print("A chave não existe.")
                    continue
            if opcao == 4:
                print("Saindo do programa...")
                raise SystemExit("Fluxo do programa foi finalizado.")
        except ValueError:
            print("O valor digitado está incorreto. Tente novamente.")
            continue
        except KeyboardInterrupt:
            print("Programa finalizado pelo usuário.")
            break


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