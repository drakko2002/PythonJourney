import tkinter as tk
from tkinter import scrolledtext

class View:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Produtor-Consumidor")

        # Botão para iniciar execução
        self.btn_iniciar = tk.Button(self.root, text="Iniciar", command=self.controller.iniciar)
        self.btn_iniciar.pack(pady=10)

        # Botão para parar execução
        self.btn_parar = tk.Button(self.root, text="Parar", command=self.controller.parar)
        self.btn_parar.pack(pady=10)

        self.execution_window = None

    def abrir_janela_execucao(self):
        """Cria uma nova janela para exibir o fluxo do código."""
        self.execution_window = tk.Toplevel(self.root)
        self.execution_window.title("Fluxo de Execução")

        self.text_area = scrolledtext.ScrolledText(self.execution_window, width=50, height=20)
        self.text_area.pack(padx=10, pady=10)

    def atualizar_fluxo(self, mensagem):
        """Atualiza a área de texto com novas mensagens."""
        if self.execution_window:
            self.text_area.insert(tk.END, mensagem + "\n")
            self.text_area.see(tk.END)

    def executar(self):
        self.root.mainloop()
