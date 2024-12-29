#a: int = int(input("Enter a number:")) #Fora do Try/Except
#b: int = int(input("Enter another number:")) #Fora do Try/Except
#Verifica-se que o problema na verdade reside entre a cadeira e o computador.

while True:
    try:
        a: int = int(input("Enter a number:"))
        b: int = int(input("Enter another number:"))
        c = float(a/b)
        print(c)
    except ZeroDivisionError:
        print("Impossível realizar operação matematica com 0.")
        continue


    except ValueError:
        print("Valor inválido!")


    except Exception as e:
        print("Erro inesperado!")
        continue
#A classe Exception é uma superclasse de exceção, que torna redundante o uso de subclasses.

    #except ValueError as e:
        #print("Que porra é essa?")
        #raise ValueError from e #Levanta um erro interno. Não preciso disso.
    break