import threading
import queue
import time
import random

class ProdutorConsumidorModel:
    def __init__(self, tamanho_fila=5):
        self.fila = queue.Queue(maxsize=tamanho_fila)
        self.evento_parada = threading.Event()
        # callbacks para view
        self.on_producao = None  # função(item, produtor)
        self.on_consumo = None   # função(item, consumidor)

    def produtor(self, nome):
        while not self.evento_parada.is_set():
            try:
                item = f"Item {random.randint(1,100)}"
                self.fila.put(item, timeout=1)
                if self.on_producao:
                    self.on_producao(item, nome)
                time.sleep(random.uniform(0.1, 0.5))
            except queue.Full:
                # fila cheia: pode notificar view se desejar
                continue

    def consumidor(self, nome):
        while not self.evento_parada.is_set():
            try:
                item = self.fila.get(timeout=1)
                if self.on_consumo:
                    self.on_consumo(item, nome)
                time.sleep(random.uniform(0.2, 0.7))
                self.fila.task_done()
            except queue.Empty:
                continue

    def iniciar(self, num_produtores=2, num_consumidores=2):
        self.evento_parada.clear()
        produtores = [threading.Thread(target=self.produtor, args=(f"P{i}",), daemon=True)
                      for i in range(num_produtores)]
        consumidores = [threading.Thread(target=self.consumidor, args=(f"C{i}",), daemon=True)
                        for i in range(num_consumidores)]
        for t in produtores + consumidores:
            t.start()
        # Threads rodam em background

    def parar(self):
        self.evento_parada.set()
