from typing import List
from typing import Self
class Soma:
    def __init__(self):
        self.numeros = [] #Para armazenar cada número.
    def adicionar(self):
        print("Digite os números a serem somados: ")
        #Corredor infinito da calculadora!
        while True:
            entrada = input("Digite um número ou 'sair' para encerrar: ")
            if entrada.lower() == "sair":
                break
        try:
            numero = float(entrada)
            self.numeros.append(numero)
        except ValueError:
            print("Esse não é um valor válido!")
    def calcularSoma():
        return sum()

    def mostrarResultado():
        #Isso é impraticável.

