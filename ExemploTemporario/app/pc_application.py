import time
from controller.producer_controller import ProducerController
from controller.consumer_controller import ConsumerController
from model.buffer_model import BufferModel
from view.console_view import ConsoleView

class PCApplication:
    def __init__(self, queue_size=3, num_producers=2, num_consumers=2, runtime=10):
        self._model = BufferModel(maxsize=queue_size)
        self._view = ConsoleView()
        self._runtime = runtime

        self._threads = [
            *[ProducerController(f"P{i}", self._model, self._view) for i in range(num_producers)],
            *[ConsumerController(f"C{i}", self._model, self._view) for i in range(num_consumers)]
        ]

    def run(self):
        for t in self._threads:
            t.start()

        time.sleep(self._runtime)
        self._model.stop_event.set()

        for t in self._threads:
            t.join()