import tkinter as tk
from tkinter import scrolledtext
import socket
import threading


class ServidorChatInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Servidor de Chat")
        self.root.geometry("500x600")

        self.txt_area = scrolledtext.ScrolledText(root, width=55, height=25)
        self.txt_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.txt_resposta = tk.Entry(root, width=45)
        self.txt_resposta.grid(row=1, column=0, padx=10, pady=10)

        self.btn_enviar = tk.Button(root, text="Enviar", command=self.enviar_resposta, state=tk.DISABLED)
        self.btn_enviar.grid(row=1, column=1, padx=10, pady=10)

        self.lbl_status = tk.Label(root, text="Servidor: Desligado")
        self.lbl_status.grid(row=2, column=0, columnspan=2, pady=5)

        self.btn_iniciar = tk.Button(root, text="Iniciar Servidor", command=self.alternar_servidor)
        self.btn_iniciar.grid(row=3, column=0, columnspan=2, pady=5)

        self.servidor_socket = None
        self.servidor_ativo = False
        self.cliente_atual = None

    def iniciar_servidor(self):
        self.servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor_socket.bind(('localhost', 12345))
        self.servidor_socket.listen(2)

        self.servidor_ativo = True
        self.lbl_status.config(text="Servidor: Aguardando conexões...")
        self.btn_iniciar.config(text="Parar Servidor")
        self.adicionar_log("Servidor iniciado. Aguardando conexões...")

        self.thread_conexoes = threading.Thread(target=self.aceitar_conexoes)
        self.thread_conexoes.daemon = True
        self.thread_conexoes.start()

    def parar_servidor(self):
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
        if not self.servidor_ativo:
            self.iniciar_servidor()
        else:
            self.parar_servidor()

    def aceitar_conexoes(self):
        while self.servidor_ativo:
            try:
                self.cliente_atual, endereco = self.servidor_socket.accept()
                self.adicionar_log(f"Cliente conectado: {endereco}")
                self.lbl_status.config(text=f"Conectado com: {endereco}")
                self.btn_enviar.config(state=tk.NORMAL)

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
                if self.servidor_ativo:
                    self.adicionar_log("Erro ao aceitar conexão")
                break

    def enviar_resposta(self):
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
        self.txt_area.insert(tk.END, f"{mensagem}\n")
        self.txt_area.see(tk.END)

    def ao_fechar(self):
        self.parar_servidor()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ServidorChatInterface(root)
    root.protocol("WM_DELETE_WINDOW", app.ao_fechar)
    root.mainloop()
