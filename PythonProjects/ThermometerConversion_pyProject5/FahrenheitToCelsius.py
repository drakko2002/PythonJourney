def fahrenheit_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
    except ValueError:
        print("Invalid Input")
        return
    _celsius = (fahrenheit - 32) * 5 / 9
    return _celsius
#Função que recebe valor explícito Fahrenheit e retorna em Celsius.