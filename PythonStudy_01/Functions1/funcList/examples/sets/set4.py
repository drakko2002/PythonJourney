#Todo: Descrição: Faça um programa que permita verificar quem esteve presente em uma reunião
# com base em duas listas diferentes de presença.
#Todo: Objetivo: Praticar operações como união, interseção e diferença de sets.
#Todo: Desafio Extra: Adicione um terceiro grupo e analise quem compareceu em todos os encontros.
def main() -> None:

    #Grupos com dicionários contendo nomes dos integrantes.
    group1 = {'Arnaldo': 22, 'Beatriz': 26, 'Fernanda': 19}
    group2 = {'Henry': 26, 'Stuart': 28, 'Ana': 22}
    group3 = {'Cedric': 21,'Basil': 22, 'Felipe': 26}

    #Dicionários para Organização dos elementos contidos nos membros.
    #grupos:dict[str,dict[str,int]] = {'grupo1': group1, 'grupo2': group2, 'grupo3': group3}
    #grupos = {'grupo1': group1, 'grupo2': group2, 'grupo3': group3}
    grupos = set(group1) | set(group2) | set(group3)

    reunion1 = set(group1) | set(group2)
    reunion2 = set(group1) | set(group3)
    reunion = reunion1 | reunion2
    #if reunion1 and reunion2 == dict:
    #    return set(reunion1) and set(reunion2)

    #Se quisermos imprimir na tela os dicionários, esse é o caminho.
    #print(f"\nDicionário de membros : {membros}\n")
    #print(f"\nDicionário de Reunião : {reunion1}\n")
    #return dict(membros) and dict(reunion1)
    #While the "return" statement returns us the obtained values, it still ends the function execution.

    participantes = []
    #for grupos in reunion1 | reunion2: #Laço referindo elementos contidos em Reunion como membros.
    intersect = grupos & reunion
    #By using the literal set converter set(grupos) it will convert the string
    #var contained in "grupos" to minor groups of strings which will become a set.

    #That's why the iteration was returning a empty set() everytime.
    intersect2 = grupos & reunion1
    intersect3 = grupos & reunion2
    print(f"Os seguintes indivíduos participaram de ambas as reuniões: {intersect}")
    print(f"Os seguintes indivíduos participaram da primeira reunião: {intersect2}")
    print(f"Os seguintes indivíduos participaram da segunda reunião: {intersect3}")
    participantes.append(intersect)



##A porra do return finaliza a execução, impedindo que a iteração passe por
#todos os grupos.




if __name__ == "__main__":
    main()

