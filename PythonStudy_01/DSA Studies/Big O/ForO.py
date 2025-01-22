numbers = [3,8,16,24,2,4,8,3]
duplicate = None
for i in range(len(numbers)):
    for j in range(i+2, len(numbers)):
        if numbers[i] == numbers[j]:
            #print(numbers[i], "is a duplicate")
            duplicate = numbers[i]
            break
for i in range(len(numbers)):
    if numbers[i] == duplicate:
        print(i)


#Na verdade eu nem sei oq isso faz.
print(numbers)
#Update: Antes, não fazia nada. Agora, compara a lista de números com dois indexadores
#diferentes para verificar a presença de duplicatas na lista.
