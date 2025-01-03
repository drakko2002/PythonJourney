'''fruits = ["apple", "banana", "cherry"]
print(len(fruits)) #Imprime o tamanho da lista com lenGHT
print(fruits) #Imprime os elementos da lista.
print(fruits[2],fruits[1],fruits[0]) #Imprime os elementos da lista na ordem designada.
#O primero elemento da lista é sempre 0.
#O último elemento da lista sempre será count -1 para sua posição da lista.
for fruit in fruits:
    if fruit == "banana": #Itera pelos elementos da lista e imprime o elemento desejado.
        print(fruit) #Se for satisfeita a condicional.
        break'''
'''Crie uma lista com 10 números inteiros.
Realize as seguintes operações:
Adicione um número ao final da lista.
Insira um número na posição 3.
Remova o último número.
Encontre e exiba o maior e o menor número na lista.
Ordene a lista em ordem crescente e decrescente.'''


def operacoes(lista):
    lista.append(int(input("Adicione um número ao final da lista: ")))
    #Prompts the user to add a num at the end of the list, making use of the
    #.append py method for list objects in python.
    #lista.__add__([3]).insert(int(input("Adiciona elemento ao terceiro lugar da lista: ")))
    lista.insert(3, int(input("Adicione elemento desejado na terceira posição da lista: ")))
    #Adiciona um elemento na terceira posição indexada da lista.
    lista.pop(-1) #Remove o último elemento da lista.
    print(f"O maior elemento da lista é {max(lista)} e o menor é {min(lista)}.")
    #Fora do loop for.
    print(lista) #Imprime a lista sem organização

    lista.sort(reverse=True)
    print(lista) #Imprime a lista agora em ordem decrescente com função nativa reverse=True

    lista.sort()
    print(lista) #Imprime a lista com função nativa sort para ordem crescente.
operacoes(lista=[1,2,3,4,5,6,7,8,9,10]) #Fornece a lista de números para ser iterada
#como parte da função python.

