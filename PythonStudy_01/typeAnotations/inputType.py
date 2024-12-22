#valor: str = input()
#print(valor)
#Nesse caso, ao inserirmos as aspas dentro do input, o Python sabe que aquilo é uma string.
#Se a entrada de dados foi uma string, então a saída também logicamente deverá ser uma string.
while True:
    try:
        valor = int(input("Digite um valor inteiro: "))
        print(valor)
        break #Pra interromper o loop se a entrada for um número inteiro.
    except ValueError:
        print("Digite uma entrada válida.")

#O propósito do bloco Try/Except é induzir um loop fadado a acontecer até que finalmente
#O valor estabelecido no bloco Except ocorra.

#Nesse caso, usamos o #ValueError que trata divergências nos valores inseridos pelo usuário.