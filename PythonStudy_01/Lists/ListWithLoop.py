numbers_list = [1, 2, 3, 4, 5]  # Renomeado para evitar sobrescrever `list`

for i in range(len(numbers_list)):  # Usar `i` como índice é mais claro
    print(numbers_list[i])  # Imprime o elemento da lista na posição `i`
    print(i + 1)  # Imprime o índice + 1

    # Um segundo loop para mostrar os índices restantes
    while i + 1 < len(numbers_list) and i + 1 < 100:
        print(i + 1)
        i += 1  # Incrementa o índice
        if i == 99:  # Evita o loop continuar infinitamente
            break
