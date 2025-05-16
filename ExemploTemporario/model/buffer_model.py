import threading
import queue

class BufferModel:
    def __init__(self, maxsize: int = 5):
        self._queue = queue.Queue(maxsize=maxsize)
        self._stop_event = threading.Event()

    def produce(self, item, timeout: float = 1):
        self._queue.put(item, timeout=timeout)

    def consume(self, timeout: float = 1):
        return self._queue.get(timeout=timeout)

    def task_done(self):
        self._queue.task_done()

    @property
    def stop_event(self):
        return self._stop_event