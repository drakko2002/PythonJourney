'''Contagem de palavras

Peça ao usuário que insira uma frase.
Conte quantas vezes cada palavra aparece e armazene essa contagem em um dicionário.
Exiba o dicionário com o formato: {palavra: contagem}.'''
def coletar() -> dict: #Por padrão, funções apontam para None. No entanto, aqui indicamos
    #Que o valor esperado é o de um dict.
    palavras_dicionario = {} #Iniciando dicionário vazio.
    frase = input("Insira uma frase: ") #Variável de requisição de input de usuário.
    palavras_listagem = frase.split() #Palavras da Frase serão quebradas e inseridas na lista.
    #Faz com que a frase seja quebrada e armazenada na variável palavras_listagem lista.
    for palavra in palavras_listagem:
        #Dentro do laço for, sugerimos que o conteúdo da lista deverá ser inserido
        #dentro do dicionário vazio anteriormente criado.
        if palavra in palavras_dicionario:
            palavras_dicionario[palavra] += 1
        #Se a palavra inserida já existir no dicionário, sua contagem será representada como +1
        #referente à contagem original de 1 e somente 1.
        else:
            palavras_dicionario[palavra] = 1
        #Se a palavra já não existir, no entanto, outrossim será inserida, porém, com um contador
        #iniciando no número 1.
    print(palavras_dicionario)
    return palavras_dicionario

#O return deve ficar sempre ao final do laço, de modo que o programa não seja finalizado
# de maneira abrupta, sem que as iterações tenham sido completadas.
coletar()
###########################

#Refatorando do zero.
