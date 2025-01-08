'''def sum(x,y) -> int:
    return int(x) + int(y)

print(sum(1,2))'''
#Why doing this when i can just do in a simpler way?
def add(x,y) -> int:
    return x+y
#The function is now set to return a concatenation between args X and Y
xis = int(input("Digite primeiro número: "))
eps = int(input("Digite segundo número: "))
#We can declare two variables to fulfill the arguments for the function aswell.


resultado = add(xis,eps)
#The new variable "result" receives the function with it's declared new arguments to
#fulfill the position of x and y.

print(resultado) #Then we print the value stored in the result function.
#As the function is set to return xy concatenation, it wont prompt a NONE value.
#Even if we dont print it, it remains the same shit.

'''def sum(x,y):
    print(x+y)
sum(4,8)
'''
#A função se comporta da exata maneira que a outra, no entanto, sem uso da função print
# e de uma variável global que salve os resultados da função.