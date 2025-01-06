#Todo-> Combinação de dados
#Todo-> Crie duas tuplas:
#Todo-> Uma com nomes de produtos.
#Todo-> Outra com os preços correspondentes.
#Todo-> Combine os dados em uma lista de tuplas no formato [(produto, preço), ...].
#Todo-> Exiba os produtos com preço acima de R$50.
a: tuple = ()
#Declara primeira tupla 'vazia'
b: tuple = ()
#Declara segunda tupla 'vazia'
lista: list = []
#Cria lista 'vazia'
for i in range(1, 10):
    #Laço FOR para [i]ndex in range(1,11)
    a = a + (f"Produto {i}",)
    #Primeira tupla concatena com a + str(produto {index}
    #E gera uma lista a partir da palavra produto e o contador "i"
    b = b + (f"R$ {i * 10}",)
    #Segunda tupla concatena str(preço) em Reais e realiza operação de multiplicação por 10
    #usando do index para gerar uma lista de preços.

lista = list(zip(a, b))
#A lista é criada a partir do empacotamento das tuplas "a" e "b"
for i in lista:
    #Chama os elementos da lista de "i" como indexador.
    if i[1] > "R$ 50":
        #Condicional para imprimir na tela os preços gerados que forem maiores que 50.
        print(i)