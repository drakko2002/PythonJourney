class A(Exception):
    pass

class B(A):
    pass

class C(B):
    pass

try:
    raise C() #Corresponde exatamente à exceção levantada.
except C: #Nesse caso, C passa a ser uma instância de si mesmo.
    print("C") #É nosso resultado.
except B:       #Continua sendo uma instância de A.
    print("B")
except A:       #É uma instância de si mesmo.
    print("A")
