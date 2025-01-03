 #Criamos vetor Y com valor 0.
'''
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
'''
def add_one(num): #Cria função add_one()
  #  if num >= 10: Isso geraria uma contagem até 10.
  #      return num #Enquanto for menor do que 10, a contagem continua.
    if num <= 10: #Cria condição booleana para num >= 10
        #Observa-se que se a condição fosse num <= 10, nada ocorreria caso
        #fosse inserido um valor menor que 10.
        '''No entanto, se fosse inserido um valor superior a 10, o resultado
        seria uma contagem infinita, visto que não há condicional booleana de interrupção
        para impedir a contagem de ir além de 10.'''
        return num #Se condição for satisfeita, retorna num.
    total = num + 1 #Cria variável total com parâmetro num_func + 1
    print(total) #Imprime o resultado de variável total na tela
    return add_one(total) #Retorna o valor da função dentro da variável total.
add_one(15) #Chama pela função com prefixo de Quinze.
#add_one(0) #Por ser menor que 10, gera uma contagem até 10.

#O código acima gera uma contagem infinita.