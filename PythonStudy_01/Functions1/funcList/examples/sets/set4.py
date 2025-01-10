#Todo: Descrição: Faça um programa que permita verificar quem esteve presente em uma reunião
# com base em duas listas diferentes de presença.
#Todo: Objetivo: Praticar operações como união, interseção e diferença de sets.
#Todo: Desafio Extra: Adicione um terceiro grupo e analise quem compareceu em todos os encontros.
def groups() -> dict:

    group1 = {'Arnaldo': 22, 'Beatriz': 26, 'Fernanda': 19}
    group2 = {'Henry': 26, 'Stuart': 28, 'Ana': 22}
    group3 = {'Cedric': 21,'Basil': 22, 'Felipe': 26}

    grupos = {'grupo1': group1, 'grupo2': group2, 'grupo3': group3}
    reunion = {'primeiro_grupo': group1, 'segundo_grupo': group2}

    print(f"\nDicionário de grupos : {grupos}\n")
    print(f"\nDicionário de Reunião : {reunion}\n")
    return dict(grupos) and dict(reunion)



def set_convert() -> set:

    return set(groups())
    #Faz do retorno de função groups um retorno em "set"

def main():
    grupos = groups()
    set_grupos = set_convert()
    




if __name__ == main():
    main()

