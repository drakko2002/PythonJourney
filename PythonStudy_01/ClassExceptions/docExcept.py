class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls() #The first Matching except clause is triggered
    #Wich means that if we swap the order ti B,C,D, it would prompt you with 3 Bs instead.
    except D: #Ele procura pela exceção levantada de cima para baixo.
        print("D") #Nesse caso, D é uma instância de C
    except C:
        print("C") #C é uma instância de B
    except B: #Classe B é a classe Base pra esse contexto, e é a primeira a ser chamada.
        print("B")