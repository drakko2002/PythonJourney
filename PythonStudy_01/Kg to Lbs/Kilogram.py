from Weight import weight
def kilogram():
    try:
        kilo  = weight() / 2.205
        print(f"O seu peso é {kilo} quilos!")
        return kilo
    except ValueError:
        print("Utilize apenas números.")