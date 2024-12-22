class Carro:
    def __init__(self, marca, modelo, cor) -> None: #Isso sempre aponta para NoneClass.
        self.marca = marca #da classe carro, self.marca equivale à marca
        self.modelo = modelo #da classe carro, self.modelo equivale à modelo
        self.cor = cor #da classe carro, self.cor equivale à cor

#Agora que isso tudo foi estabelecido nos conceitos da classe.
Hilux: Carro = Carro("Honda", "Hilux", "Prata")
#Respectivamente, o Carro Hilux rege-se pelas diretrizes marca, modelo, cor.
Honda: Carro = Carro("Honda", "Accord", "Branca")
#Respectivamente, o Carro Honda rege-se pelas diretrizes marca, modelo, cor.

#Essencialmente, podemos nos referir aos atributos que estão associados à instância do Carro.
#Ou, da classe Carro.
print(Honda.marca)
print(Honda.modelo)
print(Honda.cor)

#O conceito de classes em Python facilita a criação de objetos, ou a manipulação de objetos
#que seriam usados múltiplas vezes.

#Metódicamente, um méthodo é apenas uma função que se encontra dentro de uma classe.
#Sabemos que métodos são utilizados para manipular objetos, e induzir neles a ação desejada.

