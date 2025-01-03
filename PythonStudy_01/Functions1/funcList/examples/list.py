fruits = ["apple", "banana", "cherry"]
print(len(fruits)) #Imprime o tamanho da lista com lenGHT
print(fruits) #Imprime os elementos da lista.
print(fruits[2],fruits[1],fruits[0]) #Imprime os elementos da lista na ordem designada.
#O primero elemento da lista é sempre 0.
#O último elemento da lista sempre será count -1 para sua posição da lista.
for fruit in fruits:
    if fruit == "banana": #Itera pelos elementos da lista e imprime o elemento desejado.
        print(fruit) #Se for satisfeita a condicional.
        break
