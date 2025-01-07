'''Contagem de palavras

Peça ao usuário que insira uma frase.
Conte quantas vezes cada palavra aparece e armazene essa contagem em um dicionário.
Exiba o dicionário com o formato: {palavra: contagem}.'''
def coletar() -> dict:
    frase = input("Insira uma frase: ")
    #Solicita a frase para o usuário.

    for palavra, contagem in palavras.items():
        palavra = frase.split()
        palavras = {"palavra":palavra,"contagem":contagem}
        print(f"{palavra}: {contagem}")
        if palavra not in palavras:
            palavras[contagem] = 1
            print(palavras)
        if palavra in palavras:
            palavras[contagem] += 1
            print(palavras)
        else:
            palavras[palavra] = 1
            return palavras
    print(palavras)
coletar()
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA