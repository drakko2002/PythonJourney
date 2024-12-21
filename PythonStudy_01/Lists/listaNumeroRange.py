numero = list(range(1, 15))
print(numero)  #Aqui é a primeira iteração onde a lista tem apenas 14 elementos.
#if 5 in numero:
#    print(True)
#Ao criar uma lista de números e inserir nela a função range, o python reconhece os números
#dentro daquele escopo que você estipulou e printa eles como se fizessem parte da lista.
while numero[-1] < 20:
    numero.append(numero[-1] + 1)
    if numero[-1] == 20:
        print(numero)
        #Ao inserir a função print dentro da condicional,
        # ela só será ativada quando a condição
        #For satisfeita
        break
