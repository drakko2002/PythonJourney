def celsius_to_fahrenheit(celsius:float):
    try:
        celsius = float(celsius)
    except ValueError:
        print("Invalid Input")
        return
    _fahrenheit = (celsius * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {_fahrenheit} ")
    return _fahrenheit
#Função que recebe valor explícito de Celsius e retorna como Fahrenheit
