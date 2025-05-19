import tkinter as tk

class AFDView:
    def __init__(self, root):
        self.root = root
        self.root.title("AFD Múltiplos de 3 '0's")
        self.centralizar_janela(300, 150)

        self.label = tk.Label(root, text="Digite uma palavra sobre {0,1}:")
        self.label.pack()

        self.entrada = tk.Entry(root)
        self.entrada.pack()

        self.botao = tk.Button(root, text="Verificar")
        self.botao.pack(pady=10)

        self.resultado = tk.Label(root, text="", font=("Arial", 12))
        self.resultado.pack(pady=10)

    def set_controlador(self, controlador):
        """Vincula o controlador à View"""
        self.botao.config(command=controlador.verificar_palavra)

    def get_palavra(self):
        """Obtém o texto da entrada"""
        return self.entrada.get()

    def exibir_resultado(self, mensagem, cor):
        """Exibe o resultado na interface"""
        self.resultado.config(text=mensagem, fg=cor)

    def centralizar_janela(self, largura, altura):
        self.root.update_idletasks()
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")
