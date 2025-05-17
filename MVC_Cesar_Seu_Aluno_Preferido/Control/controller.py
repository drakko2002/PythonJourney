from MVC_Cesar_Seu_Aluno_Preferido.Model.model import ProdutorConsumidor
from MVC_Cesar_Seu_Aluno_Preferido.View.view import View
import sys
import threading

class Controller:
    def __init__(self):
        self.model = ProdutorConsumidor()
        self.view = View(self)

    def iniciar(self):
        """Inicia a execução e exibe a janela de fluxo."""
        self.view.abrir_janela_execucao()
        sys.stdout = self  # Redireciona saída para a interface gráfica
        threading.Thread(target=self.model.iniciar, daemon=True).start()

    def parar(self):
        """Finaliza a execução e fecha a interface."""
        self.model.parar()
        print("Processo encerrado!")
        if self.view.execution_window:
            self.view.execution_window.destroy()
        self.view.root.destroy()

    def write(self, mensagem):
        """Intercepta print() e envia para a interface gráfica."""
        self.view.atualizar_fluxo(mensagem)

    def flush(self):
        pass  # Necessário para compatibilidade com sys.stdout

    def executar(self):
        self.view.executar()
