def exemplo(e_nome="",e_email="",e_sobrenome=""):
#A função se define com os parâmetros posicionais já declarados como type:str nativo.
    try:
        e_nome = str(input("Digite seu nome: "))
        e_email = str(input("Digite seu email: "))
        e_sobrenome = str(input("Digite seu sobrenome: "))


        print("Nome: ", e_nome)
        print("Email: ", e_email)
        print("Sobrenome: ", e_sobrenome)
    except ValueError as erro:
        print("Erro ao imprimir os dados")
    except KeyboardInterrupt as e:
        raise SystemExit("Usuário finalizou programa.") from e

#exemplo(e_nome="",e_email="",e_sobrenome="") #Ao definir a função com determinados parâmetros
#de informação, nós criamos variáveis posicionais dentro da função para serem usadas a fim de
#Preencher tais lacunas de informação. (Nesse contexto)
exemplo()
'''Nesse contexto, pelos parâmetros posicionais já estarem definidos na própria função,
 não se faz necessário chamar pelos mesmos parâmetros posicionais a cada chamada.'''

#Contudo, se estes não estivessem declarados, seria necessário.

"""Nesse caso específico, declaramos a função em sua definição com parâmetros em strings vazias"""
#Logo, ao chamar essa função, precisamos nos referir às variáveis posicionais como strings vazias também.
