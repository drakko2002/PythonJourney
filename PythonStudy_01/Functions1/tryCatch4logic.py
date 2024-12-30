def capturar_dados(prompt: str) -> str: #Valida dados do usuário type:string
    """Função auxiliar para capturar dados do usuário com validação."""
    while True:
        try:
            valor = input(prompt).strip()
            if valor:
                return valor
        except KeyboardInterrupt:
            raise SystemExit("Usuário finalizou o programa.")
        print("Entrada inválida. Por favor, tente novamente.")


def exibir_informacoes(nome: str, email: str, sobrenome: str) -> None:
    """Exibe as informações do usuário."""
    print("\nInformações fornecidas:")
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"Sobrenome: {sobrenome}")


def executar_programa(nome: str = "", email: str = "", sobrenome: str = "") -> None:
    """Fluxo principal do programa."""
    try:
        if not nome:
            nome = capturar_dados("Digite seu nome: ")
        if not email:
            email = capturar_dados("Digite seu email: ")
        if not sobrenome:
            sobrenome = capturar_dados("Digite seu sobrenome: ")

        exibir_informacoes(nome, email, sobrenome)

    except (TypeError, ValueError):
        print("Erro ao processar os dados. Por favor, tente novamente.")
        executar_programa()
    except KeyboardInterrupt as e:
        raise SystemExit("Usuário finalizou o programa.") from e


# Chamada inicial do programa
executar_programa()
