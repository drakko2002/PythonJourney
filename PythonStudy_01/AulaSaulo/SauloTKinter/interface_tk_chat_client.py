import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

class ChatInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Cliente")
        self.root.geometry("400x500")
        
        # Área de mensagens
        self.txt_area = scrolledtext.ScrolledText(root, width=45, height=20)
        self.txt_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        # Campo de entrada
        self.entrada = tk.Entry(root, width=35)
        self.entrada.grid(row=1, column=0, padx=10, pady=10)
        
        # Botão enviar
        self.btn_enviar = tk.Button(root, text="Enviar", command=self.enviar_mensagem)
        self.btn_enviar.grid(row=1, column=1, padx=10, pady=10)
        
        # Status da conexão
        self.lbl_status = tk.Label(root, text="Desconectado")
        self.lbl_status.grid(row=2, column=0, columnspan=2, pady=5)
        
        # Botão conectar
        self.btn_conectar = tk.Button(root, text="Conectar", command=self.conectar)
        self.btn_conectar.grid(row=3, column=0, columnspan=2, pady=5)
        
        # Variáveis de conexão
        self.client_socket = None
        self.conectado = False
        
    def conectar(self):
        if not self.conectado:
            try:
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client_socket.connect(('localhost', 12345))
                self.conectado = True
                self.lbl_status.config(text="Conectado")
                self.btn_conectar.config(text="Desconectar")
                
                # Inicia thread para receber mensagens
                self.thread_receber = threading.Thread(target=self.receber_mensagens)
                self.thread_receber.daemon = True
                self.thread_receber.start()
                
                self.adicionar_mensagem("Conectado ao servidor!")
                
            except ConnectionRefusedError:
                self.adicionar_mensagem("Erro: Servidor não disponível ou lotado!")
        else:
            self.desconectar()
            
    def desconectar(self):
        if self.conectado:
            self.client_socket.close()
            self.conectado = False
            self.lbl_status.config(text="Desconectado")
            self.btn_conectar.config(text="Conectar")
            self.adicionar_mensagem("Desconectado do servidor!")
            
    def enviar_mensagem(self):
        if self.conectado:
            mensagem = self.entrada.get()
            if mensagem:
                try:
                    self.client_socket.send(mensagem.encode())
                    self.adicionar_mensagem(f"Você: {mensagem}")
                    self.entrada.delete(0, tk.END)
                except:
                    self.desconectar()
        else:
            self.adicionar_mensagem("Erro: Não conectado ao servidor!")
            
    def receber_mensagens(self):
        while self.conectado:
            try:
                mensagem = self.client_socket.recv(1024).decode()
                if mensagem:
                    self.adicionar_mensagem(f"Servidor: {mensagem}")
            except:
                break
                
    def adicionar_mensagem(self, mensagem):
        self.txt_area.insert(tk.END, mensagem + "\n")
        self.txt_area.see(tk.END)
        
    def ao_fechar(self):
        self.desconectar()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatInterface(root)
    root.protocol("WM_DELETE_WINDOW", app.ao_fechar)
    root.mainloop()
