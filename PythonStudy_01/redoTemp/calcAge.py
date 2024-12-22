from datetime import datetime


def calcAge():
    todayDate = datetime.today().year
    print(f"\n //-- O ano atual é {todayDate} --//")
    ageUser = int(input("Insira seu ano de nascimento: "))
    age = int(todayDate) - (ageUser)
    print(f"A sua idade é: {age} anos")
calcAge()