'''Crie uma lista com 20 números aleatórios entre 1 e 100.
Separe os números em duas listas: uma para pares e outra para ímpares.
Exiba o total de números pares e ímpares.'''
from random import randint
numbers = [randint(1, 100) for _ in range(20)]
pairNum = list(filter(lambda x: x % 2 == 0, numbers))
#a forma lambda é usada comumente para criar funções anónimas.
oddNum = list(filter(lambda x: x % 2 == 1, numbers))
#Nesses dois contextos, foram adicionados parâmetros para que fosse executado um MMC
#dentro dessa função, usando como base os números da função numbers[randint(a,b)
#que gera 20 números aleatórios no escopo de 1 até 100.

print(f'Pares: {pairNum}')
#Imprime os números pares.
print(f'Ímpares: {oddNum}')
#Imprime os números ímpares.
print(f'O total de números Pares é {len(pairNum)}')
#Com a função len, podemos imprimir o tamanho da lista de números pares e ímpares.
print(f'O total de números Ímpares é {len(oddNum)}')
