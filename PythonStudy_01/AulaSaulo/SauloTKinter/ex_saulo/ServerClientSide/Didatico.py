import tkinter as tk
import threading
import socket
import time


class TkinterDidatico:
    def __init__(self, root):
        self.root = root
        self.root.title("Exemplo de Tkinter com Redes")
        self.root.geometry("400x300")

        self.lbl_status = tk.Label(root, text="Status: Desconectado")
        self.lbl_status.pack(pady=10)

        self.btn_conectar = tk.Button(root, text="Conectar ao Servidor", command=self.conectar_servidor)
        self.btn_conectar.pack(pady=5)

        self.btn_desconectar = tk.Button(root, text="Desconectar", command=self.desconectar, state=tk.DISABLED)
        self.btn_desconectar.pack(pady=5)

        self.txt_mensagem = tk.Entry(root, width=50)
        self.txt_mensagem.pack(pady=5)

        self.btn_enviar = tk.Button(root, text="Enviar", command=self.enviar_mensagem, state=tk.DISABLED)
        self.btn_enviar.pack(pady=5)

        self.txt_area = tk.Text(root, width=50, height=10, state=tk.DISABLED)
        self.txt_area.pack(pady=5)

        self.cliente_socket = None
        self.conectado = False

    def conectar_servidor(self):
        self.btn_conectar.config(state=tk.DISABLED)
        threading.Thread(target=self.tentar_conectar, daemon=True).start()

    def tentar_conectar(self):
        while not self.conectado:
            try:
                self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.cliente_socket.connect(('localhost', 12345))
                self.conectado = True
                self.lbl_status.config(text="Status: Conectado")
                self.btn_enviar.config(state=tk.NORMAL)
                self.btn_desconectar.config(state=tk.NORMAL)
                self.adicionar_log("Conectado ao servidor.")
                threading.Thread(target=self.receber_mensagens, daemon=True).start()
                return
            except ConnectionRefusedError:
                self.adicionar_log("Servidor cheio. Tentando novamente em 5 segundos...")
            except Exception as e:
                self.adicionar_log(f"Erro ao conectar: {e}. Tentando novamente em 5 segundos...")
            time.sleep(5)

    def receber_mensagens(self):
        try:
            while self.conectado:
                mensagem = self.cliente_socket.recv(1024).decode()
                if not mensagem:
                    break
                self.adicionar_log(f"Servidor diz: {mensagem}")
        except:
            pass
        finally:
            self.desconectar()

    def enviar_mensagem(self):
        mensagem = self.txt_mensagem.get()
        if mensagem and self.conectado:
            try:
                self.cliente_socket.send(mensagem.encode())
                self.adicionar_log(f"Você: {mensagem}")
                self.txt_mensagem.delete(0, tk.END)
            except:
                self.adicionar_log("Erro ao enviar mensagem. Desconectado?")
                self.desconectar()

    def adicionar_log(self, mensagem):
        self.txt_area.config(state=tk.NORMAL)
        self.txt_area.insert(tk.END, f"{mensagem}\n")
        self.txt_area.config(state=tk.DISABLED)
        self.txt_area.see(tk.END)

    def desconectar(self):
        self.conectado = False
        if self.cliente_socket:
            self.cliente_socket.close()
        self.lbl_status.config(text="Status: Desconectado")
        self.btn_enviar.config(state=tk.DISABLED)
        self.btn_desconectar.config(state=tk.DISABLED)
        self.btn_conectar.config(state=tk.NORMAL)
        self.adicionar_log("Desconectado do servidor.")

    def ao_fechar(self):
        self.desconectar()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterDidatico(root)
    root.protocol("WM_DELETE_WINDOW", app.ao_fechar)
    root.mainloop()
