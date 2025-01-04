'''Crie uma lista com 5 nomes de frutas.
Pergunte ao usuário o nome de uma fruta e:
Verifique se ela está na lista.
Caso não esteja, adicione-a.
Caso esteja, remova-a.
Exiba a lista atualizada.'''
'''def string_list():
    lista_frutas = ['banana', 'laranja', 'uva', 'abacaxi', 'melancia']
        
    questiona_fruta = input("Verifique se a fruta está na lista: ")
    
    while resposta not in ["Y", "N"]:
        resposta = input("Entrada inválida. Digite Y para Yes ou N para No: ").upper()
        #Ao inserir as variáveis em um bloco próprio, isso possibilita maior uso para elas.
        print(questiona_fruta) #chama a variável para ativar os condicionais abaixo


        if questiona_fruta in lista_frutas:
            print("A fruta se encontra na lista!")
            print("\nDeseja remover a fruta? Y or N")
            print(resposta)
            if resposta == "Y":
                lista_frutas.pop(lista_frutas.index(questiona_fruta))
                print("A fruta foi removida!")
            if resposta == "N":
                print("Usuário disse não.")
                return
            

        if questiona_fruta not in lista_frutas:
            print("A fruta não está na lista...")
            print("\nDeseja adicionar a fruta? Y or N")
            print(resposta)
            if resposta == "Y":
                lista_frutas.append(questiona_fruta)
                print("A fruta foi adicionada!")
            if resposta == "N":
                raise SystemExit("Usuário finalizou programa.")
    return lista_frutas


string_list()
'''
def string_list():
    lista_frutas = ['banana', 'laranja', 'uva', 'abacaxi', 'melancia']

    questiona_fruta = input("Verifique se a fruta está na lista: ")
    #O laço FOR foi retirado, considerando que o mesmo era redundante e não contribuía
    #para o funcionamento do código.

    if questiona_fruta in lista_frutas:
        #Valida valor inserido pelo usuário em variável questiona_fruta.
        print("A fruta se encontra na lista!")
        resposta = input("Deseja remover a fruta? (Y/N): ").upper()
        #Função upper coloca carácteres inseridos em uppercase.
        while resposta not in ["Y", "N"]:
            #Inicia um loop até que a resposta seja o valor desejado.
            resposta = input("Entrada inválida. Digite Y para Yes ou N para No: ").upper()
        if resposta == "Y":
            #Se resposta do usuário for Y, if retornará True, e a condicional será executada.
            lista_frutas.pop(lista_frutas.index(questiona_fruta))
            print("A fruta foi removida!")
        else:
            print("Usuário optou por não remover a fruta.")

    else:
        #Esse bloco poderia se tornar uma função para facilitar o uso.
        print("A fruta não está na lista...")
        resposta = input("Deseja adicionar a fruta? (Y/N): ").upper()
        while resposta not in ["Y", "N"]:
            #Induz usuário em loop para que a entrada de dados seja a resposta ideal.
            resposta = input("Entrada inválida. Digite Y para Yes ou N para No: ").upper()


        if resposta == "Y":
            lista_frutas.append(questiona_fruta)
            print("A fruta foi adicionada!")
        #Se resposta do usuário for positiva, executa a adição do elemento
        #que foi salvo na variável questiona_fruta.
        else:
            print("Usuário optou por não adicionar a fruta.")

    print("Lista de frutas atualizada:", lista_frutas)
    return lista_frutas
string_list()
#O fluxo do programa se se executa razoavelmente bem.
#Talvez um loop que induza o usuário a adicionar frutas até que ele opte por sair
#seja divertido.