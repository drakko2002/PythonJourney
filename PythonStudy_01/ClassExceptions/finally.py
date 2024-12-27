def main():
    try:
        print("try") #Imprime Try em forma de string na tela.
        raise Exception("exception") #Chama a exceção como exception.
    except Exception as e: #Salva a exceção numa variável "e".
        print("except") #Imprime o texto Except ao ocorrer a exceção Exception.
    finally: #Realiza uma limpeza no código.
        print("finally") #Imprime Finally e finaliza.
if __name__ == "__main__":
    main()