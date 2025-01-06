def immutable_temp(temp) -> tuple:
    test_tuple = (1, 2, 3, 4, 5)
    try:
        a = int(temp(input("Enter a number: ")))
    except ValueError:
        print("Por favor, insira um número válido.")
        return test_tuple

    #Cria-se uma nova tupla com elementos da tupla original + os novos elementos.
    first_tuple = test_tuple + (a,)
    #We redeclared the test tuple with itself concatening with a secondary tuple
    #created by immutable_temp function parameter temp.
    print(test_tuple) #Tupla de teste
    #No entanto, a tupla de teste permanece inalterada.
    return first_tuple #Primeira tupla
second_tuple = immutable_temp(int) #Ela clona a primeira tupla numa segunda tupla.
print(second_tuple)
#second_tuple.append()
#Tuple objects has no attributes .append or .extend
#This means they cant be modified by normal means
#Which is exactly why we are trying to concatenate it with each other.
third_tuple = second_tuple + immutable_temp(float)
print(sorted(third_tuple))

#The only way of modifying a tuple after its creation is by creating a secondary tuple and
#concatenating it with each other.

