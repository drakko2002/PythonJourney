import array as arr
a = arr.array('d',[12.3,40.6,18.8,90.1,102.1])
print(sorted(a))
#Com a função nativa sorted, podemos organizar os elementos contidos no array.
#Os elementos contidos em Arrays são geralmente mutáveis.

'''O algoritmo de array acima possui o typecode (d) que implica
num elemento de tipo flutuante com 8-byte size de armazenamento.'''


#Arrays podem conter somente elementos de um mesmo tipo.
#Se o typecode corresponde a elementos do tipo inteiro, os elementos
#contidos naquele array só poderão ser do tipo inteiro.

#Cada type code possui byte-sizes diferentes e tipos de dados
#diferentes.

#Para valores de pontos flutuantes, existem os tipos 'f' e 'd'
#com 4 byte-size e 8-byte size, respetivamente.

#Para os valores inteiros, existem os typecodes 'I' e 'L' que
#possuem 4-byte size.

#Para valores inteiros menores que possam ser armazenados em
#endereços de memória menores do que 4-byte size, existem os
#type codes 'h' e 'H' com 2 byte-size.

#Para carácteres Unicode, existe o typecode 'u' com 2 byte-size.

#Para valores inteiros com 2-byte size, existem os typecodes 'i' e 'l'
