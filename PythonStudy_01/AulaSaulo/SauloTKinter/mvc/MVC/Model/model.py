class AFDModel:
    def __init__(self):
        self.estado = 0  # Estado inicial
        self.transicoes = {
            0: {'0': 1, '1': 0},
            1: {'0': 2, '1': 1},
            2: {'0': 0, '1': 2},
        }
        self.estado_final = 0  # Estado de aceitação

    def processar(self, palavra):
        """Processa a palavra e verifica se é aceita pelo autômato."""
        self.estado = 0  # Reinicia para o estado inicial
        for simbolo in palavra:
            if simbolo in self.transicoes[self.estado]:
                self.estado = self.transicoes[self.estado][simbolo]
            else:
                return False  # Símbolo inválido
        return self.estado == self.estado_final
