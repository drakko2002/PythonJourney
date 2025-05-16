class ConsoleView:
    @staticmethod
    def produced(producer_name: str, item: str):
        print(f"Produtor {producer_name} produziu: {item}")

    @staticmethod
    def producing_wait(producer_name: str):
        print(f"Fila cheia! Produtor {producer_name} aguardando...")

    @staticmethod
    def consumed(consumer_name: str, item: str):
        print(f"Consumidor {consumer_name} consumiu: {item}")

    @staticmethod
    def consuming_wait(consumer_name: str):
        print(f"Fila vazia! Consumidor {consumer_name} aguardando...")