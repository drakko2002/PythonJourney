'''Aparentemente, exceções são derivadas de uma classe base de exceções em Python. A classe
BaseExcept é aquela que origina as exceções geradas pelo Python.'''
#Se uma exceção é instância de uma classe derivada, pode-se considerar que ela também é
#Instância de sua classe base de exceções.
#Contudo, uma exceção que é instância da classe base de exceções não é considerada instância\n'
#de qualquer outra classe derivada.
class A(Exception):
    pass

class B(A):
    pass

class C(B):
    pass

try:
    raise C()  # Lança uma exceção do tipo C
except A:
    print("A") #C herda de B, que Herda de A. A é a classe base nesse caso.
except B:
    print("B") #B é uma classe derivada de A, mas A é independente de B.
except C: #C e B são subclasses de A, e por isso, não capturam exceções da classe base.
    print("C") #C é derivado de B que herdou de A, portanto, é uma ramificação de A.
#Ao chamar a exceção com Raise Exception, o python verifica de cima para baixo para ver qual
#Deles corresponde à exceção levantada.
#Pode-se observar que: A exceção C é uma instância da classe base A, que é herdada de B,
#E por sua vez, B herda de A.
#Nessa hierarquia de exceções, portanto, a execução nunca chegará nas exceções inferiores ao 'A'
#Visto que nesse contexto, a exceção levantada já foi tratada.