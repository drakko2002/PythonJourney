stock_prices_day = ['january','february','march','april','may','june','july','august'
    ,'september','october','november','december']
stock_prices_prices = [20,30,40,50,60,70,80,90,100,110,120]
dict_stock = dict(zip(stock_prices_day,stock_prices_prices))
print(f"Price in first quarter was: \n{dict_stock}\n")