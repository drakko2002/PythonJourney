def valida_dados(prompt: str) -> str:
    """Valida a entrada do usuário garantindo que não seja vazia."""
    while True:
        try:
            validador = input(prompt).strip()
            if validador:
                return validador
            else:
                raise ValueError("Erro em valor inserido.")
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            raise SystemExit("Programa finalizado.")


def captura_dados() -> dict:
    """Captura os dados do usuário e retorna como dicionário."""
    user = {
        "nome": valida_dados("Digite seu nome: "),
        "idade": valida_dados("Digite sua idade: "),
        "email": valida_dados("Digite seu email: "),
    }
    print("\nDados capturados com sucesso!")
    return user


def exibe_dados(user: dict) -> None:
    """Exibe os dados do usuário formatados."""
    print(f"\nDados do usuário:")
    for chave, valor in user.items():
        print(f"{chave.capitalize()}: {valor}")


def altera_dados(user: dict) -> None:
    """Permite ao usuário alterar campos do dicionário."""
    campos = {1: "nome", 2: "idade", 3: "email"}
    print("\nDeseja alterar algum dado?")
    for k, v in campos.items():
        print(f"{k} - {v.capitalize()}")

    try:
        opcao = int(input("Digite o número do campo a alterar (ou 0 para sair): "))
        if opcao == 0:
            return
        if opcao in campos:
            user[campos[opcao]] = valida_dados(f"Digite o novo {campos[opcao]}: ")
            print(f"{campos[opcao].capitalize()} alterado com sucesso!")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Por favor, insira um número válido.")
    except KeyboardInterrupt:
        raise SystemExit("Programa finalizado.")


def fluxo_dados():
    """Controla o fluxo principal do programa."""
    print("Bem-vindo ao sistema de cadastro!")
    user = captura_dados()
    exibe_dados(user)

    while True:
        alterar = input("\nDeseja alterar algum dado? (S/N): ").strip().upper()
        if alterar == "S":
            altera_dados(user)
            exibe_dados(user)
        elif alterar == "N":
            print("\nCadastro finalizado.")
            exibe_dados(user)
            break
        else:
            print("Opção inválida.")
    return user


# Execução principal
if __name__ == "__main__":
    fluxo_dados()
#Foi o GPT que me disse pra fazer dessa forma.
