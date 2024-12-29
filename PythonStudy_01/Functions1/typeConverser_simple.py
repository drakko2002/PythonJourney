#def convert(number):
#    if number % 2 == 0:
        #Operador é usado para iterar sob duas variáveis inteiras, dividir, e retornar
        #O módulo. Esse operador lógico se comporta diferente do seu equivalente na linguagem C
        #Visto que aqui ele retorna o resto da operação de divisão.
#        return "Even"
#    else:
#        return "Odd"
a = input("Entre com os dados: ") #Pede para que o usuário entre com os dados.
def convert_to_int(user_input): #Função que converte string para int.
    try:

        return int(user_input) # Retorna o valor inserido pelo usuário como type:int
    except ValueError: # Se o valor inserido não puder ser convertido para inteiro, retorna um erro
        raise ValueError(f"The entered value {a} is not a valid integer.")

try:
    user_input = convert_to_int(a) #Declara que user_input equivale à função convert_to_int
    print(convert_to_int(a)) #Imprime na tela o resultado da conversão, se der tudo certo.
    print(type(user_input)) #Para ter certeza que funcionou, imprime o tipo do dado convertido.
except ValueError as e:
    print(e) #Se não funcionar ele levanta uma exceção de erro de valor.