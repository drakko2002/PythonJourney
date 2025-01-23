import array as arr



b = arr.array('d',[10.5,20.5,30.8,40.9,51.18,80.4,98.1,100.5])
#No array cima, definimos o type code como 'd' que implica em valores de ponto flutuante.
#Isso significa, que o array só poderá conter valores de ponto flutuante.
for x in range(len(b)):
    print(f"First: Valor contido em posição {x} = {b[x]}")
    #Com isso, imprimimos de maneira detalhada os elementos contidos no array 'b'
print("Fim primeira iteração.\n")

for x in range(len(b[0:4])):
    print(f"Second: Valor contido em posição {x} = {b[x]}")
print("Fim segunda iteração.")
#Arrays toleram métodos de slicing, indexing, extending e derivados.
#São comumente confundidos com as listas em Python, mas a diferença entre os dois é que Listas podem conter misturas
#de elementos, enquanto Arrays podem conter um e somente um tipo de elemento, sendo que todos os elementos declarados
#no array devem corresponder ao typecode declarado a princípio.
