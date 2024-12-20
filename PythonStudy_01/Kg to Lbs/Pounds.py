from Weight import weight


def pounds():
    try:
        puds = weight() * 2.205
        print(f"O seu peso é {puds} libras!")
        return puds
    except ValueError:
        print("Digite apenas números!")
