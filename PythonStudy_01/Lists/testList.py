numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while numeros[-1] < 50: #O último elemento da lista pode ser alcançado com um simples -1
    numeros.append(numeros[-1] + 1)
    print(numeros)
    if numeros[-1] == 50:
        break