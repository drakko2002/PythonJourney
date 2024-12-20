x = int(input("Digite o X: "))
if x == 0:
    print("Digite um valor diferente de 0.")
    exit()
while x <= 15:
    print(x*'*')
    x = x+1

#Ao colocar a operação de multiplicação para concatenar integer com string dentro do próprio print,
#você faz com que a variável x passe a ter seu valor reconhecido em asteriscos, pois você multiplicou
#a variável x com aqueles asteriscos.

#Ao inserir o condicional antes de iniciar o loop, você torna o efeito dele absoluto frente ao looping proposto por while
#E se o usuário inserir um valor que seja exatamente igual a 0, o código finalizará sua execução sem prossguir com a incrementação.
