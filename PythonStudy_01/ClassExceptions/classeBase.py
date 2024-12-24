class A(Exception):
    pass

class B(A):
    pass

try:
    raise A() #Logo no início, temos A que é a classe base.
except B: #B, que é uma subclasse de A, não pode capturar exceções da classe base.
    print("B")
except A:
    print("A")
#Nesse caso, o bloco except B não captura a exceção.
#Isso se dá porque A nesse caso é nossa classe base, e não uma mera subclasse de B.
'Classe Derivada não captura classe base.'
'Classe base pode capturar classe derivada.'
