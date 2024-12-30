def exemplo(e_nome="",e_email="",e_sobrenome=""):
#A função se define com os parâmetros posicionais já declarados como type:str nativo.

    try:
        while True:
            #if not e_nome: #Com condicional IF + valor booleano NOT, ele apenas faz
            #a solicitação do nome pro usuário se o mesmo já não tiver sido fornecido.
            e_nome = str(input("Digite seu nome: ")).strip() #Precisa ficar dentro do loop.
            if e_nome:
                break
            print("O campo não pode ficar vazio.")
            #A função .strip() elimina espaços em branco na input.
            #Oq valida o nome como se não tivesse sido inserido, em teoria.
                #break #Quebra o loop se o nome for inserido.
        while True:
            #if not e_email: #Aplica-se também para o e-mail.
            e_email = str(input("Digite seu email: ")).strip()
            if e_email:
                break
            print("O campo não pode ficar vazio.")
        while True:
            #if not e_sobrenome: #Aplica-se também para o sobrenome.
            e_sobrenome = str(input("Digite seu sobrenome: ")).strip()
            if e_sobrenome:
                break
            print("O campo não pode ficar vazio.")

        print("Nome: ", e_nome)
        print("Email: ", e_email)
        print("Sobrenome: ", e_sobrenome)



    except TypeError as erro:
        print("Erro ao imprimir os dados")
    except ValueError as erro:
        print("Erro ao imprimir os dados")
        exemplo()
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
