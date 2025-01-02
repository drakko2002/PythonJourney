 #Criamos vetor Y com valor 0.
def contador(y):
    #Como queremos que o valor de Y seja incrementado
    #Ele teria que ficar fora da função, para que não fosse declarado
    #Como seu valor sendo zero a cada chamada recursiva da função.
    if y < 10:
        print(y)
        increase = y + contador(y+1)
        print(increase)
        contador(0)
    else:
        print(f"Resultado chegou em {y}")
        raise SystemExit("Fim do Programa.") from RuntimeError
    #Evita a mensagem de erro vermelha horrorosa.
contador(0)