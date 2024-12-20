numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while numeros[-1] < 50: #O último elemento da lista pode ser alcançado com um simples -1
    numeros.append(numeros[-1] + 1)
    #    print(numeros) Isso conta todas as iterações da lista até chegar no 50.
    if numeros[-1] == 50:
        print(numeros) # Então é melhor colocar a chamada dessa função dentro de uma condição de parada.
        break
        #Ao ser atingida a condição de parada, ele vai printar a lista agora com todos os elementos,
        #e ai sim vai finalizar o código.