import pandas as pd
#A razão para a pandas.lib não estar funcionando corretamente era um conflito
#que se gerou em decorrência do nome do arquivo.py que antes era Pandas

#O interpretador não sabia se ele importava o arquivo ou a lib em si.
#E como o arquivo pandas.py em questão não tinha nenhum métdo ou função
#que fosse nomeada DataFrame, nada acontecia.


# Constante para limitar o tamanho dos itens
MAX_FRUIT_COLOR = 3

# Dados das frutas e cores
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
colors = ['red', 'yellow', 'green']

# Garante compatibilidade de tamanhos
fruit_data = {
    'fruit': fruits[:MAX_FRUIT_COLOR],
    'color': colors[:MAX_FRUIT_COLOR]
}

# Criação do DataFrame
fruit_dataframe = pd.DataFrame (columns=['fruit', 'color'], data=fruit_data)
print(fruit_dataframe)