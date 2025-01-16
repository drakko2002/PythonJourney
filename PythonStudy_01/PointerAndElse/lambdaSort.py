#sorted(iterable, key=function) ordena algo com base em uma função.
palavras: list = ["Python, C#, Java, JavaScript, TypeScript"]
ordena = (sorted(palavras, key=lambda x: x.strip()))
ordena_ = (sorted(palavras, key=lambda x: len(x)))
print(ordena)
print(ordena_)