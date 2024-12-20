from PythonStudy_01.Lists.ListWithLoop import numbers_list

SMALL_THRESHOLD = 100
LARGE_THRESHOLD = 1000


def process_number(number):
    print(number + 1)
    if numbers_list < SMALL_THRESHOLD:
        print(number + 2)
    elif numbers_list < LARGE_THRESHOLD:
        print(number + 3)
    else:
        print(number + 4)


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
    process_number(number)
