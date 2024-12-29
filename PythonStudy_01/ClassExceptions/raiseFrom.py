a: int = int(input("Enter a number:"))
b: int = int(input("Enter another number:"))

while True:
    try:
        c = int(a/b)
        print(c)
        if a == str:
            print("Invalid input")
            break
        elif b == str:
            print("Invalid input")
            break
    except (ZeroDivisionError, ValueError) as e:
        print("Entrada de dados inválida!")
        print(e)
        raise ValueError from e
    break