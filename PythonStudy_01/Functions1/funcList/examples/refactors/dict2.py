def coletar() -> dict:
    palavras = {}  # Inicializa um dicionário vazio para armazenar as contagens.

    frase = input("Insira uma frase: ")
    palavras_lista = frase.split()  # Divide a frase em palavras.

    for palavra in palavras_lista:
        # Verifica se a palavra já está no dicionário.
        if palavra in palavras:
            palavras[palavra] += 1  # Incrementa a contagem.
        else:
            palavras[palavra] = 1  # Adiciona a palavra com contagem inicial de 1.

    print(palavras)  # Exibe o dicionário resultante.
    return palavras
#Desgraçado.
#Todo: Tentar reconstruir o código amanhã novamente, do zero.