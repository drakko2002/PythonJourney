#Todo: Descrição: Crie um jogo onde o programa apresenta uma frase, e o jogador precisa identificar quantas palavras únicas existem.
#Todo: Objetivo: Trabalhar com sets para remover duplicatas e contar elementos exclusivos.
#Todo: Desafio Extra: Adicione uma funcionalidade para comparar o desempenho de dois jogadores'''



def set_example():
    while True:
        print("Bem vindo ao jogo de palavras!")
        frase = input("Digite uma frase: ")
        try:
            if frase == "":
                print("Campo de frase não pode ficar vazio.")
                continue
            salva_frase = frase
            palavras_unicas = set(frase.split()) or set(salva_frase.split())

            resposta_jogador = int(input("Quantas palavras únicas existem na frase: "))
            resultado = (resposta_jogador, len(palavras_unicas))

            if resposta_jogador == len(palavras_unicas):
                print("Você acertou!")
                print("Deseja comparar desempenhos de dois jogadores?")
                pergunta = str(input("S ou N: ")).strip()
                print(pergunta)

                while pergunta not in ["S", "N", "s", "n"]:

                    try:
                        if pergunta.upper() == "S" or pergunta.upper() == "s":
                            print(resultado)

                        if pergunta.upper() == "N" or pergunta.upper() == "n":
                            print("Obrigado por jogar!")
                            break
                    except ValueError:
                        print("Digite apenas S ou N.")
                        break

            print("Obrigado por jogar!")


            if resposta_jogador != len(palavras_unicas):
                print("Você errou!")
                print("Deseja tentar de novo?")


                pergunta = str(input("S ou N: ")).strip()
                print(pergunta)




                while pergunta not in ["S","N","s","n"]:
                    try:
                        if pergunta.upper() == "S" or pergunta.upper() == "s":
                            return resposta_jogador

                        elif pergunta.upper() == "N" or pergunta.upper() == "n":
                            print("Obrigado por jogar!")
                            break
                        else:
                            print("Digite apenas S ou N.")
                            pergunta = str(input("S/N: "))
                            continue
                    except ValueError:
                        print("Digite apenas S ou N.")
                        pergunta = str(input("S/N: "))


        except KeyboardInterrupt:
            print("Usuário finalizou o programa!")
            raise SystemExit
        except TypeError:
            print("Tipo de valor não é suportado.")
            continue
        except ValueError:
            print("Valor inserido é inválido.")
            continue
set_example()