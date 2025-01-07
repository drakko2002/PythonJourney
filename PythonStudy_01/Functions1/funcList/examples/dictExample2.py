'''Contagem de palavras

Peça ao usuário que insira uma frase.
Conte quantas vezes cada palavra aparece e armazene essa contagem em um dicionário.
Exiba o dicionário com o formato: {palavra: contagem}.'''
def coletar(palavras,contador: dict) -> dict:
    #palavras = {"palavra": "contagem"}
    frase = input("Insira uma frase: ")
    palavra = frase.split()
    for i in range(len(palavra)):
        contador = (palavra.count(palavra[i]))
        palavras: dict = {"palavra": palavra, "contagem": contador}
        print(palavras)
        return palavras
coletar(palavras={},contador={})
