from datetime import datetime
anoNascimento = int(input("Digite o ano de nascimento: "))
def ano_atual() -> int:
    now = datetime.now()
    _ano_atual = now.year
    return int(_ano_atual)
calc = ano_atual() - anoNascimento
print(calc)
