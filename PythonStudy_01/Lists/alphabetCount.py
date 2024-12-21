alfabeto = []
contador = 0

for i in range(ord('A') , ord('Z') + 1):
    alfabeto.insert(contador, chr(i))
    contador += 1
    for j in range (ord('A') , ord('Z') + 1):
        alfabeto.append(chr(i)+chr(j))
print(len(alfabeto))