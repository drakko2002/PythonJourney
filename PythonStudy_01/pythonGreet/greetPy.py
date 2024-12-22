from date_greetpy import greet
from datetime import datetime
while True:
    try:
        nome = (input("Qual é o seu nome: "))
        if not nome.isalpha(): #the .isalpha() method validates the object and check if it
            #comports only alphabetic values like A to Z. It raises a ValueError if
            #it differs from the alphabetic parameter.
            raise ValueError
    except ValueError as e:
        print(e)
        print("Digite apenas letras.")
        continue
    print(f"Bom dia {nome}! Hoje é {greet()} e é um belo dia para estudar!")
    break
