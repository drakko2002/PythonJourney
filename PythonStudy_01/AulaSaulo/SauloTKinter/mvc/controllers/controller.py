class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        # Configurar apenas os callbacks dos botões
        self.view.configurar_comandos_botoes(
            self._acao_botao_1,
            self._acao_botao_2
        )

    def _acao_botao_1(self):
        self.model.registrar_acao("Botão 1 acionado")
        print("Ação 1 executada e registrada")

    def _acao_botao_2(self):
        self.model.registrar_acao("Botão 2 acionado")
        print("Ação 2 executada e registrada") 