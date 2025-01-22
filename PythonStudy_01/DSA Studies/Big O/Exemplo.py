#Consideremos uma lista em Python
def find_element(lst, target):
    for item in lst:
        if item == target:
            return True
        return False

#O bloco acima cria uma função de busca em lista, onde o parâmetro
#utilizado é uma lista, com um argumento de target.
#Nas condicionais, definimos um laço for para os itens contidos
#na lista da função.
#Se o item contido na lista corresponder ao argumento target,
#a função retorna um valor booleano True.
#Do contrário, retorna false.

'''A complexidade do algoritmo citado é O(n), onde n é o tamanho da lista.
e O deveria ser referida como a constante da equação.'''
#O(1) -> (Constante):
#O tempo não depende do tamanho da entrada.
#Exemplo: Acessar um elemento de uma lista por meio de um índice:
'''lst[0]'''
#O(log n) -> Logarítmica):
#O tempo cresce lentamente com o tamanho da entrada inserida.
#Exemplo: Busca binária em uma lista ordenada.

#O(n) -> (Linear):
#O tempo aumenta proporcionalmente ao tamanho da entrada.
#Exemplo: Percorrer a lista com iterações.

#O(n log n):
#Comum em algoritmos de ordenação eficientes, como mergesort.
#Exemplo: Ordenar uma lista com sorted(lst)

#O(n²) -> (Quadrática):
#Tempo cresce exponencialmente com a entrada. (Comumente utilizado
#em nested loops)
#Exemplo: Comparar todos os pares de elementos em uma lista.

#O(2^n) -> Notação Exponencial:
#Crescimento muito rápido, usado em problemas complexos como solução
#de certos problemas de grafos ou backtracking.

#Exemplo: Resolver o problema das N-Rainhas.
