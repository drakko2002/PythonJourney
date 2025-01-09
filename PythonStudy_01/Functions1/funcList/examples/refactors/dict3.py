def estoque_dict(estoque: dict) -> dict:
    while True:
        try:
            produto = input("Digite nome do produto (ou 'sair' para voltar ao menu): ").strip()
            if produto.lower() == 'sair':
                break
            if not produto:
                raise ValueError("Nome do produto não pode ser vazio.")

            quantidade = int(input("Digite a quantidade: "))
            if quantidade < 0:
                raise ValueError("A quantidade não pode ser negativa.")

            if produto in estoque:
                estoque[produto] += quantidade
            else:
                estoque[produto] = quantidade

            print(f"Estoque atualizado: {estoque}")
        except ValueError as e:
            print(f"Erro: {e}")
    return estoque


def atualiza_quantidade(estoque: dict) -> None:
    produto = input("Digite o nome do produto a atualizar: ").strip()
    if produto not in estoque:
        print(f"Produto '{produto}' não encontrado no estoque.")
        return

    try:
        nova_quantidade = int(input("Digite a nova quantidade: "))
        if nova_quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")

        estoque[produto] = nova_quantidade
        print(f"Estoque atualizado: {estoque}")
    except ValueError as e:
        print(f"Erro: {e}")


def remove_produto(estoque: dict) -> None:
    produto = input("Digite o nome do produto a remover: ").strip()
    if produto not in estoque:
        print(f"Produto '{produto}' não encontrado no estoque.")
        return

    estoque.pop(produto)
    print(f"Produto '{produto}' removido com sucesso.")
    print(f"Estoque atualizado: {estoque}")


def main():
    estoque = {}
    while True:
        try:
            print("\n--> Menu de Dicionários de Estoque <--")
            print("1 - Adicionar produto")
            print("2 - Atualizar quantidade")
            print("3 - Remover produto")
            print("4 - Sair")
            opcao = int(input("Digite a opção desejada: "))

            if opcao == 1:
                estoque_dict(estoque)
            elif opcao == 2:
                atualiza_quantidade(estoque)
            elif opcao == 3:
                remove_produto(estoque)
            elif opcao == 4:
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
        except KeyboardInterrupt:
            print("\nPrograma finalizado pelo usuário.")
            break


if __name__ == "__main__":
    main()
