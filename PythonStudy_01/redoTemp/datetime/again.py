from datetime import datetime
def ano_nascimento():
    while True:
        try:
            _anoNascimento = int(input("Digite o ano de nascimento: "))
            return _anoNascimento
        except ValueError:
            print("Digite apenas números!")
            continue
def ano_atual() -> int:
    now = datetime.now()
    _ano_atual = now.year
    return int(_ano_atual)
calc = ano_atual() - ano_nascimento()
print(calc)
