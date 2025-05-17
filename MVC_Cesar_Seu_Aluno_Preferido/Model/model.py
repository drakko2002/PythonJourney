import threading
import queue
import time
import random

class ProdutorConsumidor:
    def __init__(self, tamanho_fila=5):
        self.fila = queue.Queue(maxsize=tamanho_fila)
        self.evento_parada = threading.Event()
        self.produtores = []
        self.consumidores = []

    def produtor(self, nome):
        while not self.evento_parada.is_set():
            try:
                item = f"Item {random.randint(1, 100)}"
                self.fila.put(item, timeout=1)
                print(f"Produtor {nome} produziu: {item}")
                time.sleep(random.uniform(0.1, 0.5))
            except queue.Full:
                print(f"Fila cheia! Produtor {nome} aguardando...")

    def consumidor(self, nome):
        while not self.evento_parada.is_set():
            try:
                item = self.fila.get(timeout=1)
                print(f"Consumidor {nome} consumiu: {item}")
                time.sleep(random.uniform(0.2, 0.7))
                self.fila.task_done()
            except queue.Empty:
                print(f"Fila vazia! Consumidor {nome} aguardando...")

    def iniciar(self, num_produtores=2, num_consumidores=2):
        self.evento_parada.clear()
        self.produtores = [
            threading.Thread(target=self.produtor, args=(f"P{i}",)) for i in range(num_produtores)
        ]
        self.consumidores = [
            threading.Thread(target=self.consumidor, args=(f"C{i}",)) for i in range(num_consumidores)
        ]

        for t in self.produtores + self.consumidores:
            t.start()

    def parar(self):
        self.evento_parada.set()
        for t in self.produtores + self.consumidores:
            t.join()
