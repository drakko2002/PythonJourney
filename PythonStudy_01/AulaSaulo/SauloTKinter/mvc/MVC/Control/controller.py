class AFDController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controlador(self)

    def verificar_palavra(self):
        palavra = self.view.get_palavra()
        if all(c in '01' for c in palavra):
            if self.model.processar(palavra):
                self.view.exibir_resultado("Aceito! ✅", "green")
            else:
                self.view.exibir_resultado("Rejeitado ❌", "red")
        else:
            self.view.exibir_resultado("Entrada inválida! Apenas '0' e '1'.", "orange")
