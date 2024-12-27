#raise NameError('HiThere')
#Ele finaliza o código com simples menção ao nome do erro que foi informado.
def func():
    raise ConnectionError #Faz retornar um erro de conexão "gratuito"

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
#Tenta chamar a função func(), e se não for possível, chama outro erro da subclasse de exceções.
#O quadro Raise permite a inclusão de um parâmetro from.
'''O bloco acima permite a conversão de uma exceção para outra.'''