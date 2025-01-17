def fahrenheit_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
    except ValueError:
        print("Invalid Input")
        return
    _celsius = (fahrenheit - 32) * 5 / 9
    print(f"A temperatura em Celsius é: {_celsius} ")
    return _celsius
#Função que recebe valor explícito Fahrenheit e retorna em Celsius.