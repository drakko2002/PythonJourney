def cause_error(): #Função dedicada a causar um erro de divisão por zero.
    try:
        # Um erro inicial ocorre aqui
        result = 1 / 0 #Tenta realizar divisão por zero.
    except ZeroDivisionError as e: #Sugere tratamento para exceção de divisão por zero.
        # Um novo erro é lançado, automaticamente encadeando a exceção original
        raise ValueError("Erro ao tentar realizar a operação.") from e

def suppress_chaining():
    try:
        # Um erro inicial ocorre aqui
        result = int("abc")  # Isso gera um ValueError
    except ValueError:
        # Um novo erro é lançado, mas sem encadear a exceção original
        raise RuntimeError("Erro durante a conversão de dados.") from None

# Testando os casos
print("Exemplo com encadeamento de exceções:") #Está fora das funções anteriores.
#Portanto, funciona como uma espécie de cabeçalho.
try:
    cause_error() #Tenta chamar pela função que tenta dividir por zero.
except Exception as e: #Exception é uma super classe das exceções.
    print(f"Caught exception: {e}") #Imprime na tela o protocolo de erro salvo em Exception(e)
    print(f"Original cause: {e.__cause__}")  # A causa original está vinculada

#Aqui, podemos ver uma nova prática ao tratar a variável que captura a exceção Exception
#Como um objeto, ao aplicar um méthodo na variável "e"

print("\nExemplo com supressão do encadeamento:")
try:
    suppress_chaining()
except Exception as e:
    print(f"Caught exception: {e}")
    print(f"Original cause: {e.__cause__}")  # Aqui, a causa original é None
