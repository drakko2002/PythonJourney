#Todo: Fazer gestor de coleção de filmes.
#Todo: Descrição: Crie um programa que permita ao usuário adicionar, remover e listar filmes em uma coleção, garantindo que nenhum filme seja repetido.
#Todo: Objetivo: Aprender a adicionar (add) e remover (remove) elementos de um set.
#Todo: Desafio Extra: Adicione funcionalidade para verificar se um filme já está na coleção.
colecao_filmes = set() #Conjunto vazio nomeado colecao_filmes.
#Variável GLOBAL.

def validar():
    mov_var = str(input("Deseja adicionar um filme? [S/N] ")).strip().upper()
    while True:
            try:
                if mov_var == 'S':
                    print("Disse sim!")
                    return adiciona_filme()

                if mov_var == 'N':
                    print("Disse não!")
                    return menu

            except (ValueError, Exception) as error:
                print(f"Um erro ocorreu: {error}")



def adiciona_filme() -> colecao_filmes:
    #Evite usar sets() vazios recursivos dentro das funções.
    validar()

    while True:
        try:
        # Variáveis da Função.
            filme = str(input("Digite o titulo do filme: ")).strip().title()
            genero = str(input("Digite o genero do filme: ")).strip().title()

            if adiciona_filme() in colecao_filmes:
                print("O Filme já existe no catálogo!")
                break
            if adiciona_filme() not in colecao_filmes:
                print("Filme adicionado com sucesso!")
                break

            colecao_filmes.add((filme, genero))
        #Why i was calling the function inside the function?
            print("Filme adicionado com sucesso!")
            print(colecao_filmes)
        except (ValueError, Exception) as error:
            print(f"Um erro ocorreu: {error}")
            continue

'''def validar_filme(prompt:str):
    while True:
        try:'''
def listar_filmes():
    if colecao_filmes:
        print(f"A coleção contém os seguintes filmes: ")
        for filme in sorted(colecao_filmes):
            print(f"\n {filme} ")
    if not colecao_filmes:
        print("\nA coleção está vazia!")
        return None

def menu() -> colecao_filmes:
    print("1 - Adicionar filme")
    print("2 - Listar filmes")
    print("3 - Remover filme")
    print("4 - Sair")
    while True:
        opcao = int(input("Digite opção desejada: "))
        if opcao == 1:
            colecao_filmes.add(adiciona_filme())
            break
        if opcao == 2:
            print(colecao_filmes)
            break
        if opcao == 3:
            print("Remover filme")
            break
        if opcao == 4:
            raise SystemExit("Programa encerrado com sucesso!")



def main():
    print("Bem vindo ao programa de gerenciamento de filmes!")
    menu()
    return None
if __name__ == "__main__":
    main()