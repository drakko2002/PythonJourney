#list = ['apple', 'banana', 'cherry']
#for index in range(len(list)):
#    print(list[index]) #Nesse caso, o for declara o index "INDEX" para lista,e o utiliza para imprimir
#informações na tela.


#for letter in 'estudandopython':
#    if letter == 'd' or letter == 'o':
#        continue
#    print('Letra atual',letter)

#Loop for também pode ser utilizado para iterar o conteúdo de uma string.
for letter in 'estudandopython':
    pass
print("Última letra: ", letter)
#By using pass, u skip the entire word or condition and pass to the last iteration
#That would've happened.
list = ['apple', 'banana', 'cherry']
iter_obj = iter(list) #Cria um objeto iterável a partir da lista.
while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break #Exceção
#We are just calling the iter_obj declared as fruit while we iterate over it along next.
#The Fruit var was already set to iterate through the code with next and iter_object
#previously declared before the While True loop.