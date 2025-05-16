import threading  # Importa o módulo threading
import queue  # Importa o módulo queue
import time  # Importa o módulo time
import random  # Importa o módulo random

class BufferModel:
    """Modelo que encapsula a fila de itens e o evento de parada."""

    def __init__(self, maxsize: int = 5):
        self._queue = queue.Queue(maxsize=maxsize)
        self._stop_event = threading.Event()

    # --- Acesso seguro à fila ---
    def produce(self, item, timeout: float = 1):
        """Adiciona um item na fila (levanta queue.Full se exceder o timeout)."""
        self._queue.put(item, timeout=timeout)

    def consume(self, timeout: float = 1):
        """Remove e devolve um item da fila (levanta queue.Empty se exceder o timeout)."""
        return self._queue.get(timeout=timeout)

    def task_done(self):
        """Marca o processamento de um item como concluído."""
        self._queue.task_done()

    # --- Sinalização de parada ---
    @property
    def stop_event(self) -> threading.Event:
        return self._stop_event
