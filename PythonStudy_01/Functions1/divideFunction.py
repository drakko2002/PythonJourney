def divide():
    try:
        a = float(input("Digite o numerador: ")) #Pede para usuário inserir dados A.
        b = float(input("Digite o denominador: ")) #Pede para usuário inserir dados B.
        division = a / b #Tenta realizar operação de divisão com A e B fornecidos.
        print(division) #Imprime o resultado da Divisão na tela, se for bem-sucedida.

    except ZeroDivisionError as error: #Chama pela exceção ZeroDivision da classe Error,
        print(error) #Imprime detalhes do erro.
        print("Impossível dividir por zero.")


    except ValueError as error: #Chama pela exceção ValueError da classe Error.
        print(error) #Imprime detalhes do erro.
        print("Digite um valor válido.")

    except KeyboardInterrupt as error: #Chama pela Exceção KeyboardInterrupt e inicia tratamento.
        print(error)
        raise SystemExit(f"Usuário optou por finalizar programa. {error}") from error
'''Perceba que ao apagar a exceção de tratamento de erro KeyboardInterrupt, ele volta a
retornar mensagens de erro não tratadas.'''
#Quando o usuário finaliza o programa pelo atalho CTRL+C, ocorre um erro vermelho.
#Aqui, essa exceção é tratada ao causar uma outra exceção para saída do sistema.
#A saída de sistema vai imprimir o erro designado para a exceção SystemExit ao ser tratada.
divide() #Chama pela função divide.