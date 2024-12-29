#a: int = int(input("Enter a number:")) #Fora do Try/Except
#b: int = int(input("Enter another number:")) #Fora do Try/Except
#Verifica-se que o problema na verdade reside entre a cadeira e o computador.

while True:
    try:
        a: int = int(input("Enter a number:"))
        b: int = int(input("Enter another number:"))
        c = float(a/b)
        print(c)
    except ZeroDivisionError as e:
        print("Entrada de dados inválida!")
        continue


    except Exception as e:
        print("Erro inesperado!")
        continue
#A classe Exception é uma super classe de exceção, que torna redundante o uso de suas subclasses.

    #except ValueError as e:
        #print("Que porra é essa?")
        #raise ValueError from e #Levanta um erro interno. Não preciso disso.
    break