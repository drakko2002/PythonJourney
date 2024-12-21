import string
#A biblioteca string é praticamente uma biblioteca do alfabeto em si.
a = list(string.ascii_lowercase) #Aqui vemos sua aplicação no alfabeto ascii em lowercase
for letter in a:
    a.count(letter)
    print(f"Para letra {letter} temos: ", a.count(letter), "correspondentes")
print(f"Com isso, o tamanho do alfabeto é de {len(a)} letras.")
