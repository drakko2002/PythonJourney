#Todo: Crie um dicionário para armazenar produtos e suas quantidades.
#Todo: Permita que o usuário:
#Todo:  Adicione novos produtos.
#Todo:  Atualize a quantidade de um produto.
#Todo:  Remova produtos do estoque.
#Todo:  Exiba o estoque atualizado após cada operação.
'''    produto = str(input("Digite nome do produto: "))
    quantidade = int(input("Digite a quantidade: "))
    try:
        estoque[produto] = quantidade
        print(estoque)
        return estoque

    except ValueError:
        print("Erro de valor.")
estoque_dict(est)''' #Bom protótipo.
def estoque_dict(estoque:dict) -> dict:

    while True:
        try:
            #Validação da entrada do produto do usuário.
            produto = str(input("Digite nome do produto: ")).strip()
            if not produto:
                raise ValueError("Nome do produto não pode ser vazio.")
            #Fim valida entrada produto.

            #Validação da entrada da quantidade do usuário.
            quantidade = int(input("Digite a quantidade: "))
            if not quantidade:
                raise ValueError("Quantidade não pode ser nula.")
            #Fim valida entrada quantidade.

            estoque[produto] = quantidade
            #Atualiza o estoque com o produto e sua quantidade.

            print(f"Estoque atualizado: {estoque}")

            return estoque
        except ValueError as e:
            print(f"Erro: {e}")
            return estoque_dict(estoque)
        except KeyError:
            print("Houve um erro.")
            return estoque_dict(estoque)
        except KeyboardInterrupt:
            raise SystemExit("Programa finalizado pelo usuário.")

#Todo: def atualiza_quantidade(estoque:dict) -> dict:
#    produto_novo =

#Todo: def remove_produto(estoque:dict) -> dict:




def main():
    while True:
        try:
            print("-->Bem vindo ao Menu de Dicionários de Estoque <--")
            print("1 - Adicionar produto")
            print("2 - Atualizar quantidade")
            print("3 - Remover produto")
        except KeyboardInterrupt:
            raise SystemExit