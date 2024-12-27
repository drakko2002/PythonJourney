try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None
#Como é impossível abrir o banco de dados requisitado, ele chama a exceção.
'''O idioma "from None" importa um método para desabilitar chain exceptions.'''