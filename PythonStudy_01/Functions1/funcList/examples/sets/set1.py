lst = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
lst2 = [9, 9, 10, 10, 11, 11, 12, 12]
print(f"A lista é composta por: {lst} \n")
unique_lst = set(lst)
unique_lst2 = set(lst2)
print("O conjunto de únicos é formado por {}".format(unique_lst))
unique_lst3 = set(lst) | set(lst2)
#Os elementos contidos em sets não podem ser duplicados.

lst_tst1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
lst_tst2 = [3, 3, 2, 3, 3, 2, 1, 3]
unique1 = set(lst_tst1)
unique2 = set(lst_tst2)
#By using the vertical bar "|" we can combine 2 sets into a single set.
#But in the aftermath, it's still a set and it's elements cannot be duplicated.
print("Conjunto[set3]:", unique_lst3)
#We can also do it in a way without storing the combined value of the two sets into a var.
print("Combinação lista 1 e lista 2:", unique_lst | unique_lst2)
#And there's a way to show the intersection between sets.
print("Interseção entre elementos lst1 e lst2: ",unique_lst & unique_lst2)
#Althought, it wont print anything, since none of the elements contained in the sets belongs to
#the other set.
print("Interseção entre elementos lst1 e lst3: ",unique_lst & unique_lst3)
#But since the unique_lst3 var stores up the combined value of unique_lst and unique_lst2
#sets, we can apply the same method between these.


#The elements contained in "sets" cannot be duplicated.
#This means that if we have a list with a lot of duplicated numbers, but still
#we need it's representation in unique-values only, then it would be easier to convert
#The fucking list into a set.

#We can also get the difference between two sets!
print("The difference between sets is: ", unique_lst2 - unique_lst)
#In this case, the first set is the one who is going to show the difference.
#While the second set is just a check-in parameter.
'''Saída: 9, 10, 11, 12'''
print("The difference between sets is: ", unique_lst - unique_lst2)
'''Saída: 1, 2, 3, 4, 5'''

#The operation order in this case does matter, like we are asking "What does set2 have
#that set1 dont?

#Or maybe, what does set1 have that set2 doesnt??
print("The difference between sets is: ", unique1 - unique2)
#In this case, the difference between sets which means set1 has something set2 doesnt have
#is the 4, 5 numbers.
print("The difference between sets is: ", unique2 - unique1)
#Here, we see that set2 doesn't have anything that set1 already have.
#Which means that all the elements contained in set 2 are also found in set 1!

#For sake, there's a function that represents the symmetric difference.
print("The symmetric difference between sets is: ", unique_lst ^ unique_lst2)
#This function returns elements that are found in a single set, but never return elements
#that are found in BOTH sets.
#In unique list we have duplicated numbers from 1 to 5, and in unique_list2 we have elements
#counting from 9 to 10, in a duplicated symmetrical order!
'''This means that if we print the symmetrical difference between these, it will return
both the complete lists, but without it's duplicated values! Because one list does not contain
the elements contained in the other one.'''
###Another case###
print("The symmetric difference between sets is: ", unique1 ^ unique2)
#In the unique1 set we have a normal duplicated counting of 1 to 5 elements.
#In the unique2 we have a set of elements that are also contained in the list 1, in
#a random duplicated manner.
'''The only elements that are not in unique2 is 4 and 5.'''
#Which means that those elements are contained in one set, but not in the another set.

"Sets are unordered collections, differently of lists, that allows printing X element"
"In a Y position inside the list."

def lst():
    lst = [1, 2, 3, 4, 5]
    set1 = set(lst)
    #We first created a list with 1,2,3,4,5
    #Then we proceed to converting it into a set.
    try:
        print(set1[1])
    except (TypeError,Exception,RuntimeError) as error:
        print(error)
        print("We cannot perform such action inside a set.")
lst()
#We get to know that a "set" object is not subscriptable by such data manipulation method.
'''This also means that a "set" object does not support indexing, slicing, and other
data manipulation methods like those we use in lists or other data structures.'''
#We can also manipulate the boolean values to check for an element inside a set!
if 1 in unique_lst:
    print("The element is in unique list!")