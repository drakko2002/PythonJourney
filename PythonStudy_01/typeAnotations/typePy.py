#nome = "Gabriel"
#Aqui, temos uma string, mas sem a notação de tipo.
#nome: str = "Gabriel"
#Aqui, temos o mesmo nome, mas com anotação de tipo.
#nome1: str = input("Digite seu nome: ")
nome1: str = input("Digite seu nome: ")
print(nome1)
nome2: str = input("Digite seu sobrenome: ")
soma_nomes = nome1 + " " + nome2
print(soma_nomes)
#Ao converter a entrada de dados do usuário para string e declarar para o python
#Que o tipo de dado esperado naquela entrada é pra ser uma string
#No entanto, isso não evita que o Python trate aquele dado como um outro tipo de dado.

#Anotações de tipo são meramente uma ferramenta para o desenvolvedor, e não afetam a ordem
#dos acontecimentos no código. Elas não alteram a forma como o python interpreta e executa o código.