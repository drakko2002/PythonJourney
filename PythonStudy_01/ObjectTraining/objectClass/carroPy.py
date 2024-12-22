from typing import Self
class Carro:
    def __init__(self, marca: str, modelo: str, cor:str):# -> None: #Isso sempre aponta para NoneClass.
        self.marca = marca #da classe carro, self.marca equivale à marca
        self.modelo = modelo #da classe carro, self.modelo equivale à modelo
        self.cor = cor #da classe carro, self.cor equivale à cor


    def description(self):
        return f'Carro da marca {self.marca}, modelo {self.modelo} e cor {self.cor}'
    #Função description foi criada pra contornar o overflow.
    ##Ela implementa um método que retorna informações.
    def __str__(self):
        return self.description() #Toda vez que se referir à classe carro por meio de um objeto
    #Que for uma string, você terá agora retornada as informações do método description.

    def __add__(self, other):
        return self.description() + other.description()

    #Agora é possível concatenar um carro e outro numa operação de soma.


#Agora que isso tudo foi estabelecido nos conceitos da classe.
Hilux: Carro = Carro("Hilux", "Pickup", "Prata")
#Respectivamente, o Carro Hilux rege-se pelas diretrizes marca, modelo, cor.
Honda: Carro = Carro("Honda", "Accord", "Branca")
#Respectivamente, o Carro Honda rege-se pelas diretrizes marca, modelo, cor.



#Essencialmente, podemos nos referir aos atributos que estão associados à instância do Carro.
#Ou, da classe Carro.
def carro1() -> str:
    return Hilux.description() #Fazer um print(carro1()) é redundante nesse ponto.
#Ao referir-se à função, você causa uma overflow, pois está chamando uma função que foi criada
#Para chamar uma informação dentro da função. Isso é inconsistente.

def carro2() -> str:
    return Honda.description() #Fazer um print (carro2()) é redundante nesse ponto.




#O conceito de classes em Python facilita a criação de objetos, ou a manipulação de objetos
#que seriam usados múltiplas vezes.

#Metódicamente, um metodo é apenas uma função que se encontra dentro de uma classe.
#Sabemos que métodos são utilizados para manipular objetos, e induzir neles a ação desejada.
