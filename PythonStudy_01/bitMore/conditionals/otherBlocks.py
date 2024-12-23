x = int(input("Insira o número: "))
if x < 10:
    print("x is less than 10")
elif x < 20:
    print("x is less than 20")
elif x > 20:
    print("x is greater than 20")
elif x == 20:
    print("x is 20")
    print("x is equal to 20")
elif x == 5:
    print("You entered 5")
else:
    print("X is not much bigger than 5.")

    #Usuário pode inserir entrada de dados e esperar pelo prompt.
    #Pode haver quantas cláusulas ELIF o programador quiser inserir.
    #Isso é arbitrário.
    #A cláusula ELSE, por outro lado, é única. Ela deve ser designada sempre
    #Ao final do bloco.
    '''Se não fizer nenhuma das coisas acima, faça isso.'''