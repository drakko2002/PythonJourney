from views.view import View
from models.model import Model

class Controller:
    def __init__(self, model, root):
        self.model = model
        self.view = View(root, self)

    def cadastrar(self):
        # Obtém os dados do formulário
        dados = self.view.get_dados_formulario()
        print(dados)
        
        # Tenta cadastrar no banco de dados
        if self.model.cadastrar(dados['nome'], dados['email'], dados['senha']):
            print("Cliente cadastrado com sucesso!")
            self.view.limpar_formulario()  # Limpa o formulário após cadastro
        else:
            print("Erro ao cadastrar cliente!")

    def eliminar(self):
        print("Função eliminar ainda não implementada")

    def alterar(self):
        print("Função alterar ainda não implementada")
