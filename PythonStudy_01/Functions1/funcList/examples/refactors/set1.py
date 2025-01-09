def set_example():
    print("Bem-vindo ao jogo de palavras únicas!")

    while True:
        frase = input("\nDigite uma frase: ").strip()
        if not frase:
            print("A frase não pode estar vazia. Tente novamente.")
            continue

        palavras_unicas = set(frase.split())
        resposta_jogador = int(input("Quantas palavras únicas existem na frase? "))

        if resposta_jogador == len(palavras_unicas):
            print("Parabéns, você acertou!")
        else:
            print(f"Você errou! A resposta correta é {len(palavras_unicas)}.")

        comparar = input("Deseja comparar o desempenho com outro jogador? (S/N): ").strip().upper()
        if comparar == "S":
            resposta_segundo_jogador = int(input("Jogador 2, quantas palavras únicas existem na frase? "))
            if resposta_segundo_jogador == len(palavras_unicas):
                print("Jogador 2 acertou!")
            else:
                print(f"Jogador 2 errou! A resposta correta é {len(palavras_unicas)}.")
        elif comparar == "N":
            print("Obrigado por jogar!")

        jogar_novamente = input("Deseja jogar novamente? (S/N): ").strip().upper()
        if jogar_novamente != "S":
            print("Até a próxima!")
            break
