import tkinter as tk
from tkinter import scrolledtext
import socket
import threading
import queue


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
        self.clientes_conectados = []
        self.fila_espera = queue.Queue()

    def iniciar_servidor(self):
        self.servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor_socket.bind(('localhost', 12345))
        self.servidor_socket.listen(5)

        self.servidor_ativo = True
        self.lbl_status.config(text="Servidor: Aguardando conexões...")
        self.btn_iniciar.config(text="Parar Servidor")
        self.adicionar_log("Servidor iniciado. Aguardando conexões...")

        threading.Thread(target=self.aceitar_conexoes, daemon=True).start()

    def parar_servidor(self):
        self.servidor_ativo = False
        for cliente in self.clientes_conectados:
            cliente.close()
        self.clientes_conectados.clear()
        if self.servidor_socket:
            self.servidor_socket.close()

        self.lbl_status.config(text="Servidor: Desligado")
        self.btn_iniciar.config(text="Iniciar Servidor")
        self.adicionar_log("Servidor encerrado")

    def alternar_servidor(self):
        if not self.servidor_ativo:
            self.iniciar_servidor()
        else:
            self.parar_servidor()

    def aceitar_conexoes(self):
        while self.servidor_ativo:
            try:
                cliente, endereco = self.servidor_socket.accept()

                if len(self.clientes_conectados) < 5:
                    self.clientes_conectados.append(cliente)
                    self.adicionar_log(f"Cliente conectado: {endereco}")
                    self.lbl_status.config(text=f"Conectados: {len(self.clientes_conectados)}")
                    threading.Thread(target=self.tratar_cliente, args=(cliente,), daemon=True).start()
                else:
                    self.fila_espera.put(cliente)
                    self.adicionar_log(f"Fila de espera: {self.fila_espera.qsize()} clientes")
            except:
                break

    def tratar_cliente(self, cliente):
        try:
            while self.servidor_ativo:
                mensagem = cliente.recv(1024).decode()
                if not mensagem:
                    break
                self.adicionar_log(f"Cliente diz: {mensagem}")
        except:
            pass
        finally:
            cliente.close()
            self.clientes_conectados.remove(cliente)
            self.adicionar_log("Cliente desconectado")
            if not self.fila_espera.empty():
                novo_cliente = self.fila_espera.get()
                self.clientes_conectados.append(novo_cliente)
                threading.Thread(target=self.tratar_cliente, args=(novo_cliente,), daemon=True).start()
            self.lbl_status.config(text=f"Conectados: {len(self.clientes_conectados)}")

    def enviar_resposta(self):
        mensagem = self.txt_resposta.get()
        if mensagem:
            for cliente in self.clientes_conectados:
                try:
                    cliente.send(mensagem.encode())
                except:
                    pass
            self.adicionar_log(f"Servidor diz: {mensagem}")
            self.txt_resposta.delete(0, tk.END)

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
