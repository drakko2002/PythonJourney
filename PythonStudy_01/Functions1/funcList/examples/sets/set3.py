#Todo: Fazer gestor de coleção de filmes.
#Todo: Descrição: Crie um programa que permita ao usuário adicionar, remover e listar filmes em uma coleção, garantindo que nenhum filme seja repetido.
#Todo: Objetivo: Aprender a adicionar (add) e remover (remove) elementos de um set.
#Todo: Desafio Extra: Adicione funcionalidade para verificar se um filme já está na coleção.
colecao_filmes = set() #Conjunto vazio nomeado colecao_filmes.
#Variável GLOBAL.

def validar() -> None:
    mov_var = str(input("Deseja adicionar um filme? [S/N] ou 'menu' -> ")).strip().upper()
    while True:
            try:
                if mov_var not in ['S','N','MENU'] or len(mov_var) < 1:
                    raise ValueError

                elif mov_var == 'MENU':
                    return menu()

                elif mov_var == 'S':
                    print("Disse sim!")
                    break

                elif mov_var == 'N':
                    print("Disse não!")
                    break
                else:
                    raise ValueError("Quê?")


            except (ValueError, Exception) as error:
                print(f"Um erro ocorreu: {error}")

                return validar()



def adiciona_filme() -> colecao_filmes:
    #Evite usar sets() vazios recursivos dentro das funções.


    while True:
        try:
            validar()

        # Variáveis da Função.
            filme = str(input("Digite o titulo do filme: ")).strip().title()
            genero = str(input("Digite o genero do filme: ")).strip().title()


            if (filme,genero) in colecao_filmes:

                print("O Filme já existe no catálogo!")
                return menu()

            if (filme,genero) not in colecao_filmes:

                print("Filme adicionado com sucesso!")
                colecao_filmes.add((filme, genero))
                print(colecao_filmes)

                return menu()

            #colecao_filmes.add((filme, genero))

        #Why i was calling the function inside the function?
            #print("Filme adicionado com sucesso!")
            #print(colecao_filmes)
        except (ValueError, Exception) as error:
            print(f"Um erro ocorreu: {error}")
            continue
        return colecao_filmes




def listar_filmes():
    print("Selecionou listar filmes!")
    if colecao_filmes: #Verifica se coleção contém algo através de operação booleana.
        print(f"A coleção contém os seguintes filmes: ")
        for filme in sorted(colecao_filmes):
            print(f"\n {filme} ")
    if not colecao_filmes:
        print("\nA coleção está vazia!")
        return menu()

def menu() -> colecao_filmes:

    print("1 - Adicionar filme")
    print("2 - Listar filmes")
    print("3 - Remover filme")
    print("4 - Sair")
    while True:
        opcao = int(input("Digite opção desejada: "))
        if opcao == 1:
            adiciona_filme()

            break
        if opcao == 2:
            listar_filmes()
            return menu()#Eu tinha colocado pra imprimir o set ao invés de chamar a função kkkk
        if opcao == 3:
            print("Remover filme")
            remover_filme()
        if opcao == 4:
            raise SystemExit("Programa encerrado com sucesso!")



def remover_filme():
    print("Selecionou remover filme!")
    if colecao_filmes:
        listar_filmes()
        filme = str(input("Digite o titulo do filme: ")).strip().title()
        genero = str(input("Digite o genero do filme: ")).strip().title()
        if (filme,genero) in colecao_filmes:
            colecao_filmes.remove((filme,genero))
            print(f"O filme {filme} foi removido com sucesso!")
            print(f"O catálogo de filmes foi atualizado: {colecao_filmes}")

def main():
    print("Bem vindo ao programa de gerenciamento de filmes!")
    try:
        menu()
    except KeyboardInterrupt:
        raise SystemExit("Programa encerrado pelo usuário.")

if __name__ == "__main__":
    main()