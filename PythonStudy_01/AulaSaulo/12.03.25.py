class AutomatoFinitoDeterministico:
    def __init__(self, estados, estado_inicial, estados_finais):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estado_atual = estado_inicial
        self.estados_finais = estados_finais

    def transicao(self, entrada):
        if self.estado_atual == 'q0':
            if entrada == '0':
                self.estado_atual = 'q1'
            else:
                self.estado_atual = 'q0'
        elif self.estado_atual == 'q1':
            if entrada == '0':
                self.estado_atual = 'q2'  # Encontramos "00" no meio
            else:
                self.estado_atual = 'q0'
        elif self.estado_atual == 'q2':
            self.estado_atual = 'q3'  # Transição para estado válido
        elif self.estado_atual == 'q3':
            if entrada in '01':
                self.estado_atual = 'q3'  # Permanece no estado de aceitação
            else:
                self.estado_atual = 'q0'  # Retorna para Dump/lixo por ter carácter desconhecido

    def checa_simbolos(self, palavra):
        self.estado_atual = self.estado_inicial
        for simbolo in palavra:
            self.transicao(simbolo)
        return self.estado_atual in self.estados_finais

    def main(self):
        palavras_teste = ['110011', '00011', '101100', '0101', '10001', '011000']
        for palavra in palavras_teste:
            print(f"Palavra '{palavra}' aceita? {self.checa_simbolos(palavra)}")

if __name__ == "__main__":
    automato = AutomatoFinitoDeterministico({'q0', 'q1', 'q2', 'q3'}, 'q0', {'q3'})
    automato.main()