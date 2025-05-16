import threading
import random
import time
import queue

class ProducerController(threading.Thread):
    def __init__(self, name, model, view):
        super().__init__(name=name)
        self._model = model
        self._view = view

    def run(self):
        while not self._model.stop_event.is_set():
            try:
                item = f"Item {random.randint(1, 100)}"
                self._model.produce(item, timeout=1)
                self._view.produced(self.name, item)
                time.sleep(random.uniform(0.1, 0.5))
            except queue.Full:
                self._view.producing_wait(self.name)