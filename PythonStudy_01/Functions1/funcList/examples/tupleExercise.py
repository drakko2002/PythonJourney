'''Crie duas tuplas:
Uma com nomes de produtos.
Outra com os preços correspondentes.
Combine os dados em uma lista de tuplas no formato [(produto, preço), ...].
Exiba os produtos com preço acima de R$50.'''

a: tuple = () #Tupla A declarada globalmente
b: tuple = () #Tupla B declarada globalmente.
lista: list = []
#It's important to typecast so we know what we are expecting.
for i in range(1, 20): #Laço for que redeclara as tuplas A e B dentro do próprio laço.

    a = a + (f"Produto + {i}",)
    #Ao concatenar tuplas, devemos sempre nos atentar às vírgulas ao final de cada argumento.

    b = b + (f"R$ {i * 10}",)
    lista = list(zip(a, b)) #Empacota os valores contidos em tupla A e B.
    #Redeclaramos a lista para que ela realize a concatenação do conteúdo em tupla A e B + contador index I.
'''O sufixo ZIP serve para empacotar os valores contidos em tupla A e B e redeclarálos como
sendo valores contidos dentro da lista.'''
    #print(lista) Nessa linha, nós imprimimos a lista.
    #Aqui nós imprimimos uma lista com as informações armazenadas em tupla A e B
for i in lista:
    lista = i
    if lista[1] > "R$ 50":
        print(lista)
