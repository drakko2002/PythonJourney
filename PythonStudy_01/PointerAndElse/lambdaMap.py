numlist = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x**2, numlist))
#A função map aplica uma função a cada um dos elementos de uma iterável.
'''Pra esse caso, nossa iterável é uma lista de números.'''
#
print(quadrados)
#A função lambda executa uma operação de raiz quadrada com os argumentos inseridos.
#Nesse caso, os argumentos inseridos estavam dentro de uma lista de números.
'''Como resultado, cada um dos algarismos presentes na lista foram elevados ao quadrado.'''
#O resultado disso reside na variável 'quadrados' que por sua vez já guarda a função lambda dentro de si.
