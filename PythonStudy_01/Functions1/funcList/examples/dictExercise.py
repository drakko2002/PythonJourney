#Todo: Cadastro de usuários

#Todo: Crie um dicionário para armazenar informações de um usuário (nome, idade, email).
#Todo: Permita que o usuário insira os dados e os armazene no dicionário.
#Todo: Exiba as informações formatadas.
#Todo: Pergunte ao usuário se ele deseja alterar algum campo e atualize o dicionário.'''

#user: dict = {} #Dicionário vazio com nome user.
#Descontinuado o uso da variável global.
'''Para declarar dicionários de forma implícita, utilizamos chaves {}.'''
'''def captura_dados():
    while True:
        try:
            captura_nome = input("Digite seu nome: ")
            captura_idade = input("Digite sua idade: ")
            captura_email = input("Digite seu email: ")
            validador = captura_nome, captura_idade, captura_email
            user['Nome: '] = captura_nome.strip()
            user['Idade: '] = captura_idade.strip()
            user['Email: '] = captura_email.strip()
            if validador:
                print("Dados capturados com sucesso!")
            else:
                raise ValueError("Erro em valor inserido.")
            break
        except ValueError as e:
            print(e)
            continue
''' #Em tese, isso não é praticável.
def valida_dados(prompt: str) -> str: #Declara a variável da função como type:string
    while True:
        try:
            validador = input(prompt).strip()
            if validador:
                return validador
            else:
                raise ValueError("Erro em valor inserido.")
        except ValueError as e:
            print(e)
            continue
        except KeyboardInterrupt:
            raise SystemExit("Programa finalizado.")
    print("Entrada de dados é inválida. Tente novamente.")


def exibe_dados(nome: str, idade: str, email: str) -> dict:
    print(f"Nome: {nome}\nIdade: {idade}\nEmail: {email}")
    return user


def captura_dados(nome: str = "", idade: str = "", email: str = "") -> dict:
    try:
        if not user:
            user['Nome: '] = valida_dados("Digite seu nome: ")
            user['Idade: '] = valida_dados("Digite sua idade: ")
            user['Email: '] = valida_dados("Digite seu email: ")
        #Bloco dedicado a obter dados do usuário e validar entradas de dados
        #pelo usuário, através da função valida_dados com parâmetro prompt da função
        #definido para receber string.

        exibe_dados(user['Nome: '], user['Idade: '], user['Email: '])
    except ValueError as e:
        print("Tente novamente.")
        print(e)
        return captura_dados(nome, idade, email)
    except KeyboardInterrupt:
        raise SystemExit("Programa finalizado.")

#Todo: print(user) #Linha para verificar se os valores foram inseridos devidamente no dicionário.



def altera_dados(nome: str = "", idade: str = "", email: str = "") -> dict:
    confirma = str(input("Deseja alterar os dados? (S/N): "))
    if confirma.upper() == "S":
        try:
            opcao = int(input("Qual dado deseja alterar? (1-Nome, 2-Idade, 3-Email): "))
            if opcao == 1:
                altera_nome = valida_dados("Digite seu novo nome: ")
                user['Nome: '] = altera_nome
                return  user
                #Variável dentro da função definida
            #Com parâmetros invocando função de validação de entrada.
            if opcao == 2:
                altera_idade = valida_dados("Digite sua nova idade: ")
                user['Idade: '] = altera_idade
                return  user
            #Variável dentro de função definida com parâmetros que invocam função de validação.
            if opcao == 3:
                altera_email = valida_dados("Digite seu novo email: ")
                user['Email: '] = altera_email
                return user
            # Variável dentro de função definida com parâmetros que invocam função de validação.


        except ValueError as e:
            print("Tente novamente.")
            print(e)
            return altera_dados(nome, idade, email)
        except KeyboardInterrupt:
            raise SystemExit("Programa finalizado.")
        finally:
            print("Dados alterados com sucesso!")


    if confirma.upper() == "N":
        print("Usuário confirmou dados inseridos.")
        print(f"Nome: {user['Nome: ']}\nIdade: {user['Idade: ']}\nEmail: {user['Email: ']}")
        exibe_dados(user['Nome: '], user['Idade: '], user['Email: '])
        return user
def fluxo_dados():
    while True:
        try:
            print("Deseja iniciar o programa?")
            print("1 - Sim")
            print("2 - Não")
            _resposta = int(input("Digite o número da opção desejada: "))
            if _resposta == 1:
                captura_dados()
                altera_dados()
            elif _resposta == 2:
                print("Programa encerrado.")
                print(f"{user}")
                break
        except ValueError:
            print("Opção inválida.")
        except KeyboardInterrupt:
            raise SystemExit("Programa encerrado.")
        finally:
            print(f"Dados atualizados: {user}")
            return

fluxo_dados()