def main():
    print("Digite 1 para Cubo")
    print("Digite 2 para Soma")
    print("Digite 3 para Verificar Par")
    print("Digite 4 para Verificar Ímpar")
    print("Digite 5 para Sair")

    # Funções lambda definidas.
    cubo = lambda x: x ** 3
    soma = lambda x, y, z: x + y + z
    par = lambda x: x % 2 == 0
    impar = lambda x: x % 2 != 0

    while True:
        try:
            opcao = int(input("Digite a opção desejada: "))
            
            if opcao == 1:  # Cubo
                digito1 = int(input("Digite um número: "))
                print(f"O cubo de {digito1} é {cubo(digito1)}")
                #Utilizando .format para executar lambda dentro dos placeholders.

            elif opcao == 2:  # Soma
                digito1 = int(input("Digite o primeiro número: "))
                digito2 = int(input("Digite o segundo número: "))
                digito3 = int(input("Digite o terceiro número: "))
                print(f"A soma é {soma(digito1, digito2, digito3)}")

            elif opcao == 3:  # Verificar par
                digito1 = int(input("Digite um número: "))
                if par(digito1):
                    print(f"{digito1} é par.")
                else:
                    print(f"{digito1} não é par.")

            elif opcao == 4:  # Verificar ímpar
                digito1 = int(input("Digite um número: "))
                if impar(digito1):
                    print(f"{digito1} é ímpar.")
                else:
                    print(f"{digito1} não é ímpar.")

            elif opcao == 5:  # Sair
                print("Saindo do programa...")
                raise SystemExit("Programa encerrado com sucesso!")

            else:  # Caso a opção não seja válida
                print("Opção inválida. Tente novamente.")

        except ValueError:  # Entrada inválida
            print("Erro: Digite um número válido.")
        except KeyboardInterrupt:  # Interrupção manual (Ctrl+C)
            raise SystemExit("Programa encerrado pelo usuário.")

if __name__ == "__main__":
    main()
