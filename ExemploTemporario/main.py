import threading  # Importa o módulo threading
import queue  # Importa o módulo queue
import time  # Importa o módulo time
import random  # Importa o módulo random


# Este código implementa o padrão Produtor-Consumidor usando threads e uma fila sincronizada
# como uma classe que permite:
#
# - Múltiplos produtores e consumidores rodando simultaneamente
# - Controle de parada via evento
# - Timeout na fila para evitar bloqueios indefinidos
# - Tratamento de fila cheia/vazia
# - Nomeação das threads para melhor depuração
#
# A classe ProdutorConsumidor encapsula:
# - Uma fila thread-safe com tamanho máximo configurável
# - Um evento para sinalizar parada
# - Métodos produtor() e consumidor() que rodam em threads separadas
# - Método iniciar() que cria e gerencia as threads

class ProdutorConsumidor:
    def __init__(self, tamanho_fila=5):
        self.fila = queue.Queue(maxsize=tamanho_fila)  # Cria uma fila com capacidade máxima de 5 itens
        self.evento_parada = threading.Event()  # Cria um evento para sinalizar parada

    def produtor(self, nome):
        while not self.evento_parada.is_set():  # Enquanto o evento de parada não estiver setado
            try:
                # Produz item
                item = f"Item {random.randint(1, 100)}"  # Produz um item aleatório

                # Tenta colocar na fila
                self.fila.put(item, timeout=1)  # Tenta colocar o item na fila com um timeout de 1 segundo
                print(f"Produtor {nome} produziu: {item}")  # Imprime o item produzido

                # Simula trabalho
                time.sleep(
                    random.uniform(0.1, 0.5))  # Simula o trabalho com um tempo aleatório entre 0.1 e 0.5 segundos

            except queue.Full:
                print(f"Fila cheia! Produtor {nome} aguardando...")  # Imprime uma mensagem de fila cheia

    def consumidor(self, nome):
        while not self.evento_parada.is_set():  # Enquanto o evento de parada não estiver setado
            try:
                # Tenta pegar item da fila
                item = self.fila.get(timeout=1)  # Tenta pegar um item da fila com um timeout de 1 segundo
                print(f"Consumidor {nome} consumiu: {item}")  # Imprime o item consumido

                # Simula processamento
                time.sleep(
                    random.uniform(0.2, 0.7))  # Simula o processamento com um tempo aleatório entre 0.2 e 0.7 segundos

                # Marca como concluído
                self.fila.task_done()  # Marca a tarefa como concluída

            except queue.Empty:
                print(f"Fila vazia! Consumidor {nome} aguardando...")  # Imprime uma mensagem de fila vazia

    def iniciar(self, num_produtores=2, num_consumidores=2):  # Inicia as threads produtoras e consumidoras
        # Cria threads produtoras
        produtores = [  # Cria uma lista de threads produtoras
            threading.Thread(
                target=self.produtor,
                args=(f"P{i}",)
            ) for i in range(num_produtores)
        ]

        # Cria threads consumidoras
        consumidores = [  # Cria uma lista de threads consumidoras
            threading.Thread(
                target=self.consumidor,
                args=(f"C{i}",)
            ) for i in range(num_consumidores)
        ]

        # Inicia todas as threads
        for t in produtores + consumidores:
            t.start()  # Inicia a thread

        # Executa por 10 segundos
        time.sleep(10)  # Espera 10 segundos

        # Sinaliza parada
        self.evento_parada.set()  # Sinaliza o evento de parada

        # Espera todas terminarem
        for t in produtores + consumidores:
            t.join()  # Espera todas as threads terminarem


# Uso
if __name__ == "__main__":
    pc = ProdutorConsumidor(tamanho_fila=3)  # Cria uma instância da classe ProdutorConsumidor com uma fila de tamanho 3
    pc.iniciar(num_produtores=2, num_consumidores=2)  # Inicia as threads produtoras e consumidoras