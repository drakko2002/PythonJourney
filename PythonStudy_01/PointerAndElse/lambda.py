dobro = lambda x: x * 2
argumento = int(input("Digite o número a ser dobrado: "))
print(dobro(argumento))
#Nesse caso, guardamos o valor estabelecido da função lambda em ma variável chamada Dobro
#A função lambda irá executar uma operação de multiplicação por dois com o argumento.
#O argumento a ser inserido na função lambda é aquele guardado na variável argumento.
'''Observa-se que ao inserir 8, a função lambda é executada e retorna o resultado 16.'''
#Funções LAMBDA não permitem funções muito complexas ou elaboradas ao longo de múltiplas linhas.
#São usadas na maioria das vezes para executar operações simples.

#Funções lambda, por sua vez, podem ter vários argumentos, mas uma única expressão.
#possíveis aplicações giram em torno de funções de ordem superior, como map, sorted e Filter.
