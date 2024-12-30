def capturar_dados(prompt: str) -> str: #Valida dados do usuário type:string
    """Função auxiliar para capturar dados do usuário com validação."""
    while True: #Inicia loop
        try: #Tenta obter dados por meio do input do usuário com o parâmetro da função
            #de captura dos dados.
            valor = input(prompt).strip() #.strip() elimina espaços em branco no input inserido.
            #Valor é uma variável da função capturar dados, na verdade. o input(prompt).strip()
            #Apenas chama pela função prompt, e não se substitui por um input do usuário.

            #Por outro lado, isso levaria o input(prompt) a esperar uma entrada do usuário
            #Após ter imprimido a mensagem contida na variável prompt.

            if valor: #Condicional sem parâmetro de execução acaba verificando se a variável é verdadeira.
                return valor #Se for falsa, ela quebra a execução do condicional if.
        except KeyboardInterrupt: #Trata erro de KeyboardInterrupt
            raise SystemExit("Usuário finalizou o programa.") #Imprime mensagem de goodbye na tela.
        print("Entrada inválida. Por favor, tente novamente.") #Se ao final do loop try/except, o campo
        #requisitado estiver em branco, ele vai pedir novamente para que sejam inseridos dados.
        #Isso ocorrerá até que a condição seja satisfeita.


def exibir_informacoes(nome: str, email: str, sobrenome: str) -> None:
    """Exibe as informações do usuário."""
    print("\nInformações fornecidas:") #Cabeçalho indicando as informações de maneira amigável.
    print(f"Nome: {nome}") #Recebe o nome inserido
    print(f"Email: {email}") #Imprime o e-mail inserido.
    print(f"Sobrenome: {sobrenome}") #Imprime o sobrenome inserido.


def executar_programa(nome: str = "", email: str = "", sobrenome: str = "") -> None:
    """Fluxo principal do programa."""
    #Com o uso de typecast: str = "", indicamos para o interpretador que o valor esperado
    #é o de uma string, e com as aspas duplas, indicamos o gancho para a conversão de quaisquer
    #valores inseridos para string.
    try: #Tenta validar as entradas para ver se está tudo certo.

        if not nome:
            nome = capturar_dados("Digite seu nome: ")
            #Valida a entrada de nome do usuário para ver se foi fornecida.
            #Nesse caso, a variável nome da função executar_programa se define
            #Pelo uso da função de validação capturar_dados, conquanto que o prompt da função
            #Agora teria contido nele uma mensagem de "Digite seu Nome:

        if not email:
            email = capturar_dados("Digite seu email: ")
            #Valida a entrada de E-Mail do usuário para ver se foi fornecida.

        if not sobrenome:
            sobrenome = capturar_dados("Digite seu sobrenome: ")
            #Valida a entrada de sobrenome do usuário para ver se foi fornecida.

        exibir_informacoes(nome, email, sobrenome)
        #Chama pela função exibir_informaçoes(Parece conter redundância.

    except (TypeError, ValueError):
        #Trata erros do tipo digitação e valor.
        print("Erro ao processar os dados. Por favor, tente novamente.")
        #Mensagem amigável ao usuário, informando que algo errado aconteceu.
        executar_programa() #Ele não finaliza o código ao tratar esses erros.

        #Chama pela função executar_programa() do fluxo principal do programa.
    except KeyboardInterrupt as e:
        raise SystemExit("Usuário finalizou o programa.") from e
#Ao interromper o programa por meio de um atalho, o programa será finalizado
#Com uma mensagem amigável.

# Chamada inicial do programa
executar_programa()
