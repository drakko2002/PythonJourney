import tkinter as tk


class AFD:
    def __init__(self):
        self.estado = 0  # Estado inicial
        self.transicoes = {
            0: {'0': 1, '1': 0},
            1: {'0': 2, '1': 1},
            2: {'0': 0, '1': 2},
        }
        self.estado_final = 0  # Estado de aceitação

    def processar(self, palavra):
        self.estado = 0  # Reinicia para o estado inicial
        for simbolo in palavra:
            if simbolo in self.transicoes[self.estado]:
                self.estado = self.transicoes[self.estado][simbolo]
            else:
                return False  # Símbolo inválido
        return self.estado == self.estado_final


class Aplicacao:
    def __init__(self, root):
        self.afd = AFD()
        self.root = root
        self.root.title("AFD Múltiplos de 3 '0's")

        self.centralizar_janela(300, 150)

        self.label = tk.Label(root, text="Digite uma palavra sobre {0,1}:")
        self.label.pack()

        self.entrada = tk.Entry(root)
        self.entrada.pack()

        self.botao = tk.Button(root, text="Verificar", command=self.verificar_palavra)
        self.botao.pack(pady=10)

        self.resultado = tk.Label(root, text="", font=("Arial", 12))
        self.resultado.pack(pady=10)

    def verificar_palavra(self):
        palavra = self.entrada.get()
        if all(c in '01' for c in palavra):
            if self.afd.processar(palavra):
                self.resultado.config(text="Aceito! ✅", fg="green")
            else:
                self.resultado.config(text="Rejeitado ❌", fg="red")
        else:
            self.resultado.config(text="Entrada inválida! Apenas '0' e '1'.", fg="orange")

    def centralizar_janela(self, largura, altura):
        self.root.update_idletasks()
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")


if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacao(root)
    root.mainloop()