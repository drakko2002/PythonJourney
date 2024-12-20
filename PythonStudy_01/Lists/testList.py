numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    print(numero)
    if numero < 50:
        numeros.append((numero+1))
    elif numero == 50:
        break
