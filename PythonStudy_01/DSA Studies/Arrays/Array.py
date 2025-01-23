stock_prices_day = ['january','february','march','april','may','june','july','august'
    ,'september','october','november','december']
stock_prices_prices = [20,30,40,50,60,70,80,90,100,110,120]
dict_stock = list(zip(stock_prices_day,stock_prices_prices))
print(dict_stock[1])
#Retorna o valor referente à mês/preço na segunda posição indexada da lista.
#A primeira posição indexada por padrão é sempre 0.
print(f"Price in first month of the year was: {dict_stock[0]}")