numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x%2 == 0,numlist))
print(pares)
#A função lambda recebe os argumentos armazenados na iterável "numlist" e aplica neles
#a metodologia estabelecida nos parâmetros da função.

'''Com x: x%2 == 0 estabelecemos uma função lambda que recebe um argumento "x" e retorna esse
mesmo argumento 'x' dividido por 2, sob a condição de que o resto da divisão seja zero.'''

