class PCApplication:
    def __init__(self, *, queue_size: int = 3, num_producers: int = 2, num_consumers: int = 2, runtime: int = 10):
        self._model = BufferModel(maxsize=queue_size)
        self._view = ConsoleView()
        self._runtime = runtime

        # Instancia controladores (threads)
        self._threads: List[threading.Thread] = [
            *[ProducerController(f"P{i}", self._model, self._view) for i in range(num_producers)],
            *[ConsumerController(f"C{i}", self._model, self._view) for i in range(num_consumers)],
        ]

    def run(self):
        # Inicia todas as threads
        for t in self._threads:
            t.start()

        # Tempo de execução
        time.sleep(self._runtime)

        # Solicita parada
        self._model.stop_event.set()

        # Aguarda término das threads
        for t in self._threads:
            t.join()
