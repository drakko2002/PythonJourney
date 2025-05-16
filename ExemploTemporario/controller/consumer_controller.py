import threading
import time
import random
import queue

class ConsumerController(threading.Thread):
    def __init__(self, name, model, view):
        super().__init__(name=name)
        self._model = model
        self._view = view

    def run(self):
        while not self._model.stop_event.is_set():
            try:
                item = self._model.consume(timeout=1)
                self._view.consumed(self.name, item)
                time.sleep(random.uniform(0.2, 0.7))
                self._model.task_done()
            except queue.Empty:
                self._view.consuming_wait(self.name)