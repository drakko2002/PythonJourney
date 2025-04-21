import tkinter as tk
from models.model import Model
from views.view import View
from controllers.controller import Controller

def main():
    print("Iniciando a aplicação")
    root = tk.Tk()
    print("Criando a janela")
    model = Model()
    print("Criando o modelo")
    view = View(root) # Observe que o objeto view é criado com o root como argumento!
    print("Criando a view")
    controller = Controller(model, view)
    print("Criando o controller")
    root.mainloop()


if __name__ == "__main__":
    main() 
