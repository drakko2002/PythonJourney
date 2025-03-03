
estadooo: int = 0


def digitar(estado):
    match estado:
        case 0:
            palavra = int(input("digite sua palavra"))
            if (palavra == 1):
                estado = 0
            elif (palavra == 0):
                estado = 1
            print(estado)
        case 1:
            palavra = int(input("digite sua palavra"))
            if (palavra == 1):
                estado = 3
            elif (palavra == 0):
                estado = 2
            print(estado)
        case 2:
            palavra = int(input("digite sua palavra"))
            if (palavra == 1):
                estado = 3
            elif (palavra == 0):
                estado = 3
            print(estado)
        case 3:
            print("palavra aceita")
while (estadooo != 3):
    digitar(estadooo)


