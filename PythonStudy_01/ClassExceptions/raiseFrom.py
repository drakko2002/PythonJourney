a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
while True:
    try:
        c = a/b
        print(c)
        break
    except ZeroDivisionError as e:
        print("An error has occurred.")
        raise ValueError("Division by zero is not allowed") from e
    continue
