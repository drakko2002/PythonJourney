import threading
from models import model
from views import view

class ProdutorConsumidorController:
    def __init__(self, model: model, view: view):
        self.model = model
        self.view = view
        # conecta eventos model->view
        self.model.on_producao = self.view.adicionar_producao
        self.model.on_consumo = self.view.adicionar_consumo
        # conecta view->controller
        self.view.bind_start(self.start)
        self.view.bind_stop(self.stop)

    def start(self):
        # inicia model em thread separada para não bloquear a UI
        threading.Thread(target=self.model.iniciar, daemon=True).start()
        self.view.on_started()

    def stop(self):
        self.model.parar()
        self.view.on_stopped()
