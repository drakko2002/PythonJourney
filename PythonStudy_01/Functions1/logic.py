from tryCatch4logic import capturar_dados
prompt = "Digite algo: "
valor = input(prompt).strip()  # Suponha que o usuário digita "   Olá   "

# Após o .strip(), `valor` será "Olá"

if valor:
    print("Você digitou:", valor)  # Será exibido "Você digitou: Olá"
else:
    print("Você não digitou nada.")  # Não será exibido neste caso
