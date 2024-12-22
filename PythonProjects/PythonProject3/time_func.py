import time
def timeFunction():
    anoAtual = time.localtime().tm_year #adicionando um int no inicio para converter o tipo da classe.
#Na teoria, o time é um objeto, e localtime() é um méthod para obter o tempo atual do sistema.
    #tm_year, por sua vez, obtém apenas o dado de tempo associado ao ano.
    #A saída original fica: (tm_year=2024, tm_mon=12,
    # tm_mday=22, tm_hour=13, tm_min=56,
    # tm_sec=54, tm_wday=6,
    # tm_yday=357, tm_isdst=0)
    return int(anoAtual)
timeFunction()
