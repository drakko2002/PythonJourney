import tkinter as tk
from tkinter import scrolledtext

class InterfaceDidatica:
    def __init__(self, root):
        # Configura a janela principal
        self.root = root
        self.root.title("Interface Didática")
        self.root.geometry("400x500")  # Largura x Altura

        '''
        Explicação de como posicionar os widgets dentro do root:
        - root é o widget pai
            self.txt_area
            self.txt_entrada
            self.btn_enviar
            self.lbl_status
            self.btn_limpar são widgets filhos do root

        - Todos os filhos possuem uma propriedade grid.
          O grid é uma propriedade que define a posição do widget dentro do root.
          O grid é uma grade de linhas e colunas.
          O widget será posicionado na intersecção da linha e coluna.

            row: linha
            column: coluna
            columnspan: quantidade de colunas que o widget irá ocupar
             
        '''
        self.txt_area = scrolledtext.ScrolledText(
            root,          # widget pai
            width=45,      # largura em caracteres
            height=20      # altura em linhas
        )
        self.txt_area.grid(
            row=0,         # primeira linha
            column=0,      # primeira coluna
            columnspan=2,  # ocupa 2 colunas
            padx=10,       # margem horizontal
            pady=10        # margem vertical
        )
        
        # Campo de txt_entrada de texto
        self.txt_entrada = tk.Entry(
            root,          # widget pai
            width=35       # largura em caracteres
        )
        self.txt_entrada.grid(
            row=1,         # segunda linha
            column=0,      # primeira coluna
            padx=10,
            pady=10
        )
        
        # Botão de enviar
        self.btn_enviar = tk.Button(
            root,
            text="Enviar",
            command=self.enviar_mensagem  # função chamada ao clicar
        )
        self.btn_enviar.grid(
            row=1,         # segunda linha
            column=1,      # segunda coluna
            padx=10,
            pady=10
        )
        
        # Label de status
        self.lbl_status = tk.Label(
            root,
            text="Status: Pronto"
        )
        self.lbl_status.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=5
        )
        
        # Botão adicional
        self.btn_limpar = tk.Button(
            root,
            text="Limpar",
            command=self.limpar_tela
        )
        self.btn_limpar.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=5
        )
    
    def enviar_mensagem(self):
        """Função chamada quando o botão Enviar é clicado"""
        # Pega o texto do campo de txt_entrada
        mensagem = self.txt_entrada.get()
        
        if mensagem:  # Se houver texto
            # Adiciona a mensagem na área de texto
            self.txt_area.insert(tk.END, f"Mensagem: {mensagem}\n")
            # Limpa o campo de txt_entrada
            self.txt_entrada.delete(0, tk.END)
            # Rola para o final do texto
            self.txt_area.see(tk.END)
            # Atualiza o status
            self.lbl_status.config(text="Status: Mensagem enviada")
    
    def limpar_tela(self):
        """Função chamada quando o botão Limpar é clicado"""
        # Limpa a área de texto
        self.txt_area.delete(1.0, tk.END)
        # Atualiza o status
        self.lbl_status.config(text="Status: Tela limpa")

# Cria e inicia a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceDidatica(root)
    root.mainloop()
