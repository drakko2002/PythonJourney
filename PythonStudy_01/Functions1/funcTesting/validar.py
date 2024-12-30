def valida_dados(valid: str) -> str:
    """Captura e valida a entrada do usuário."""
    while True:
        try:
            valor = input(valid).strip()
            if valor:
                '''A metodologia replace se mostrou incompatível com o código sendo feito.'''
            #if valor and valor.replace(" ", "").replace("-",
            #    "").replace("'", "").replace("@","").replace("_","").replace(
            #    ".","").isalpha():

                return valor
                #Verifica também se variável valor possui apenas letras para que a entrada seja válida.
            print("Entrada vazia ou Inválida. Tente novamente.")
            print("Certifique-se de digitar apenas letras para o nome e sobrenome.")
        except KeyboardInterrupt:
            raise SystemExit("Usuário finalizou o programa.")


def valida_email(prompt: str) -> str:
    """Captura e valida um e-mail no formato correto."""
    while True:
        email = valida_dados(prompt)
        if "@" in email and email.count("@") == 1:
            return email
        print("E-mail inválido. Por favor, insira um endereço válido (com '@').")


def imprime_dados(nome: str, sobrenome: str, email: str) -> None:
    """Exibe as informações do usuário formatadas."""
    print("\nInformações fornecidas:")
    print(f"Nome: {nome}")
    print(f"Sobrenome: {sobrenome}")
    print(f"E-mail: {email}")


def main() -> None:
    """Fluxo principal do programa."""
    while True:
        try:
            nome = valida_dados("Digite o nome: ")
            sobrenome = valida_dados("Digite o sobrenome: ")
            email = valida_email("Digite o e-mail: ")

            imprime_dados(nome, sobrenome, email)
            break  # Sai do loop principal ao concluir com sucesso

        except (ValueError, TypeError):
            print("Erro no valor inserido. Por favor, tente novamente.")
        except KeyboardInterrupt:
            raise SystemExit("Usuário finalizou o programa.")


# Execução do programa
main()
