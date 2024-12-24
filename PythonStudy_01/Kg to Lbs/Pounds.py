from Weight import weight


def pounds():
    try:
        puds = weight() * 2.205
        print(f"O seu peso é {puds} libras!")
        return puds
    except (ValueError, TypeError, ZeroDivisionError): #Bloco Except permite tratamento
        #de múltiplos erros de uma só vez. (Eu não sabia)
        print("Digite um valor válido!")
