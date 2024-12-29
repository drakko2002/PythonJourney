a = int(input("Enter a number:"))
b = int(input("Enter another number:"))

while True:
    try:
        c = int(a/b)
        print(c)
    except (ZeroDivisionError, ValueError) as e:
        print("An error has occurred.")
        break
