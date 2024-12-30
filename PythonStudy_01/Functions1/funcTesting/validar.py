def valida_dados(valid: str) -> str: #Indica que o valor esperado é uma string.

    while True:

        try:
            valor = input(valid).strip()


            if valor:
                return valor


            #break #Se quebrarmos aqui, o except e o print acabam por não serem executados.
        except KeyboardInterrupt:
            raise SystemExit("Usuário finalizou o programa.")
        print("Erro no valor inserido.")

def imprime_dados(nome: str, sobrenome: str, email: str) -> None:
    print("Nome: {}\nSobrenome: {}\nE-mail: {}".format(nome, sobrenome, email))
    #Quando usando a função .format para organizar as informações de uma string, não
    #se pode utilizar do parâmetro "f" antes da porra da string.

def main(nome: str = "", sobrenome: str = "", email: str = "") -> None:
    while True:
        try:
            if not nome:
                nome = valida_dados("Digite o nome: ")

            if not sobrenome:
                sobrenome = valida_dados("Digite o sobrenome: ")

            if not email.count("@") == 1:
                email = valida_dados("Digite o e-mail: ")

            imprime_dados(nome, sobrenome, email)



        except KeyboardInterrupt:
            raise SystemExit("Usuário finalizou o programa.")


        except (ValueError, TypeError):
            print("Erro no valor inserido para o campo especificado.")
            main()  # Chama função principal.

        finally:
            while True:
                try:
                    if not nome or not sobrenome or not email:
                        continue
                    if nome and sobrenome and not email:
                        email = valida_dados("Digite o e-mail: ")
                        if email.count("@") != 1:
                            raise TypeError("Modelo de e-mail é inválido.")
                    if nome and sobrenome and email:
                        break
                    else:
                        break
                except SystemExit("Impossível continuar."):
                    break


