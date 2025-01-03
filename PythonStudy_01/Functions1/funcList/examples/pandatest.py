import pandas as pd

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
