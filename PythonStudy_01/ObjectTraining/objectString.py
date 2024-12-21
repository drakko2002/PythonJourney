a = "Hello World, i'm a object!"
print(f'O tipo literal da classe é: {type(a)}')
#Nesse contexto, var "a" está sendo tratada como o objeto da classe string.
#Seu comportamento é geralmente ditado por métodos associados ao seu tipo de classe.
while type(a) is str:
    print(a.upper())
    #Os parenteses extras de .upper estão associados ao self-apply do métod da classe.
    break
#Nisso, a saída será em uppercase, e depois tratará a execução do código como terminada.
