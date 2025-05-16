import threading  # Importa o módulo threading
import queue  # Importa o módulo queue
import time  # Importa o módulo time
import random  # Importa o módulo random

class ProducerController(threading.Thread):
    """Thread controladora de produção."""

    def __init__(self, name: str, model: BufferModel, view: ConsoleView):
        super().__init__(name=name)
        self._model = model
        self._view = view

    def run(self):
        while not self._model.stop_event.is_set():
            try:
                # Gera um item aleatório
                item = f"Item {random.randint(1, 100)}"
                # Tenta inserir no buffer
                self._model.produce(item, timeout=1)
                self._view.produced(self.name, item)
                # Pausa simulando trabalho
                time.sleep(random.uniform(0.1, 0.5))
            except queue.Full:
                self._view.producing_wait(self.name)

class ConsumerController(threading.Thread):
    """Thread controladora de consumo."""

    def __init__(self, name: str, model: BufferModel, view: ConsoleView):
        super().__init__(name=name)
        self._model = model
        self._view = view

    def run(self):
        while not self._model.stop_event.is_set():
            try:
                # Tenta retirar do buffer
                item = self._model.consume(timeout=1)
                self._view.consumed(self.name, item)
                # Pausa simulando processamento
                time.sleep(random.uniform(0.2, 0.7))
                # Indica conclusão do item
                self._model.task_done()
            except queue.Empty:
                self._view.consuming_wait(self.name)