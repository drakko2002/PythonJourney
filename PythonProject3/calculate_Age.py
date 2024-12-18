from time_func import timeFunction

birth_year = int(input("What's the birthyear: "))
actual_year = int(timeFunction())

calc_Age = actual_year - birth_year

print(calc_Age)



print("A idade do individuo é: ", calc_Age)