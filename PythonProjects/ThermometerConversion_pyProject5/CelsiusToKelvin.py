def celsius_to_kelvin(celsius):
    try:
        _kelvin = celsius + 273.15
        print(f"A temperatura em Kelvin é: {_kelvin}" )
        return _kelvin
    except ValueError:
        print("Invalid Input")
        return