import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

class ServidorChatInterface:
    def __init__(self, root):
        # Configura a janela principal
        self.root = root
        self.root.title("Servidor de Chat")
        self.root.geometry("500x600")
        
        # Área de log do servidor
        self.txt_area = scrolledtext.ScrolledText(root, width=55, height=25)
        self.txt_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        # Campo de resposta
        self.txt_resposta = tk.Entry(root, width=45)
        self.txt_resposta.grid(row=1, column=0, padx=10, pady=10)
        
        # Botão enviar resposta
        self.btn_enviar = tk.Button(
            root,
            text="Enviar",
            command=self.enviar_resposta,
            state=tk.DISABLED  # Começa desabilitado
        )
        self.btn_enviar.grid(row=1, column=1, padx=10, pady=10)
        
        # Status do servidor
        self.lbl_status = tk.Label(root, text="Servidor: Desligado")
        self.lbl_status.grid(row=2, column=0, columnspan=2, pady=5)
        
        # Botão iniciar/parar servidor
        self.btn_iniciar = tk.Button(
            root,
            text="Iniciar Servidor",
            command=self.alternar_servidor
        )
        self.btn_iniciar.grid(row=3, column=0, columnspan=2, pady=5)
        
        # Variáveis do servidor
        self.servidor_socket = None
        self.servidor_ativo = False
        self.cliente_atual = None
        
    def iniciar_servidor(self):
        """Inicia o servidor em uma thread separada"""
        self.servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor_socket.bind(('localhost', 12345))
        self.servidor_socket.listen(5)
        
        self.servidor_ativo = True
        self.lbl_status.config(text="Servidor: Aguardando conexões...")
        self.btn_iniciar.config(text="Parar Servidor")
        self.adicionar_log("Servidor iniciado. Aguardando conexões...")
        
        # Inicia thread para aceitar conexões
        self.thread_conexoes = threading.Thread(target=self.aceitar_conexoes)
        self.thread_conexoes.daemon = True
        self.thread_conexoes.start()
    
    def parar_servidor(self):
        """Para o servidor e fecha todas as conexões"""
        self.servidor_ativo = False
        if self.cliente_atual:
            self.cliente_atual.close()
        if self.servidor_socket:
            self.servidor_socket.close()
        
        self.lbl_status.config(text="Servidor: Desligado")
        self.btn_iniciar.config(text="Iniciar Servidor")
        self.btn_enviar.config(state=tk.DISABLED)
        self.adicionar_log("Servidor encerrado")
    
    def alternar_servidor(self):
        """Alterna entre iniciar e parar o servidor"""
        if not self.servidor_ativo:
            self.iniciar_servidor()
        else:
            self.parar_servidor()
    
    def aceitar_conexoes(self):
        """Thread que aceita conexões de clientes"""
        while self.servidor_ativo:
            try:
                self.cliente_atual, endereco = self.servidor_socket.accept()
                self.adicionar_log(f"Cliente conectado: {endereco}")
                self.lbl_status.config(text=f"Conectado com: {endereco}")
                self.btn_enviar.config(state=tk.NORMAL)
                
                # Recebe mensagens do cliente
                while True:
                    try:
                        mensagem = self.cliente_atual.recv(1024).decode()
                        if not mensagem:
                            break
                        self.adicionar_log(f"Cliente diz: {mensagem}")
                    except:
                        break
                
                self.cliente_atual.close()
                self.cliente_atual = None
                self.btn_enviar.config(state=tk.DISABLED)
                self.lbl_status.config(text="Servidor: Aguardando conexões...")
                self.adicionar_log("Cliente desconectado")
                
            except:
                if self.servidor_ativo:  # Se não foi parada intencional
                    self.adicionar_log("Erro ao aceitar conexão")
                break
    
    def enviar_resposta(self):
        """Envia resposta para o cliente atual"""
        if self.cliente_atual and self.servidor_ativo:
            resposta = self.txt_resposta.get()
            if resposta:
                try:
                    self.cliente_atual.send(resposta.encode())
                    self.adicionar_log(f"Servidor diz: {resposta}")
                    self.txt_resposta.delete(0, tk.END)
                except:
                    self.adicionar_log("Erro ao enviar resposta")
    
    def adicionar_log(self, mensagem):
        """Adiciona mensagem na área de log"""
        self.txt_area.insert(tk.END, f"{mensagem}\n")
        self.txt_area.see(tk.END)
    
    def ao_fechar(self):
        """Chamado quando a janela é fechada"""
        self.parar_servidor()
        self.root.destroy()

# Inicia a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = ServidorChatInterface(root)
    root.protocol("WM_DELETE_WINDOW", app.ao_fechar)
    root.mainloop()
