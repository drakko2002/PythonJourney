import tkinter as tk
from tkinter import messagebox
#Nome: César Augusto Rapelli de Oliveira
#R.A: 4200935

class AFDMultiploDe3Zeros:
    def __init__(self):
        """Essa função serve para inicializar o autômato num dado estado inicial."""
        self.estado_atual = "q0"

    def reset(self):
        """a linha abaixo faz o autômato voltar ao estado inicial/original"""
        self.estado_atual = "q0"

    def transicao(self, simbolo):
        """abaixo temos um dicionário com as palavras compatíveis com o alfabeto"""
        transicoes:dict = {
            "q0": {"0": "q1", "1": "q0"},
            "q1": {"0": "q2", "1": "q1"},
            "q2": {"0": "q0", "1": "q2"},
        }
        self.estado_atual = transicoes[self.estado_atual][simbolo]

    def aceita(self, palavra):
        """essa função realiza uma verificação das palavras inseridas"""
        self.reset() #Se não for aceita a palavra, o autômato volta para o estado inicial.

        for simbolo in palavra: #Aqui a sugestão que o Giovani fez em sala, mas implementada corretamente.
            if simbolo not in {"0", "1"}:
                raise ValueError(f"Entrada inválida: '{simbolo}'. Use apenas '0' e '1'.")
            self.transicao(simbolo) #Se houver uma palavra não reconhecida pelo alfabeto, o autômato recusa
            #e levanta uma exceção de erro no valor inserido.

        return self.estado_atual == "q0" #Após cad aoperação o autômato retorna para seu estado inicial
    #De modo a permitir a inserção de várias palavras sem que vc precise fechar a janela


class InterfaceAFD:
    def __init__(self, root):
        """iniciamos a interface gráfica do autômato"""
        self.root = root
        self.root.title("Autômato Múltiplo de 3 Zeros")
        self.root.geometry("400x250")

        self.afd = AFDMultiploDe3Zeros()

        # Label de instrução
        self.label = tk.Label(root, text="Digite uma palavra (apenas 0s e 1s):")
        #Aqui definimos a frase que o usuário verá para ter sua experiência guiada.
        self.label.pack(pady=15) #aq definimos o tamanho e espaçamento das instruções

        # Campo de entrada
        self.entrada = tk.Entry(root, width=30) #aqui, definimos a largura do campo de texto
        self.entrada.pack(pady=5) #Aqui definimos o espaçamento

        # Botão para verificar
        self.btn_verificar = tk.Button(root, text="Verificar Palavra", command=self.verificar_palavra)
        #A linha acima dá as instruções do q acontece se vc clicar no botão, e chama a função de verificação.
        self.btn_verificar.pack(pady=10) #Eu admito, eu coloquei tamanho 100 aqui pq eu pensei que ia ficar pequeno

        # Label de resultado
        self.resultado = tk.Label(root, text="", font=("Arial", 12, "bold")) #Fonte e texto para leitura assertiva
        self.resultado.pack(pady=10) #Espaçamento, como sempre. n pode esquecer, né?

    def verificar_palavra(self):
        """Verifica se a palavra é aceita pelo AFD e exibe o resultado."""
        palavra = self.entrada.get().strip() #Aqui nós temos a implementação de uma função de classe
        #onde tentamos verificar se palavra se encontra no alfabeto com "if not palavra"
        # e se não estiver, levantamos a clássica exceção de erro do valor inserido.
        try:
            if not palavra:
                raise ValueError("A entrada não pode estar vazia.")

            aceita = self.afd.aceita(palavra)
            #Aqui, chamamos a função primária de aceite da palavra, onde ocorre uma verificação mais simples
            # e uma comunicação entre essas duas funções
            if aceita:
                self.resultado.config(text="Palavra aceita ✅", fg="green")
            else:
                self.resultado.config(text="Palavra rejeitada ❌", fg="red")

        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            self.resultado.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceAFD(root)
    root.mainloop()
#O inicializador prevê o início de root como tkinter, por fim, após inicializada a biblioteca
#temos o início do aplicativo de interface, e com isso, chamamos novamente o objeto root com um método
#que implementa o mainloop()

'''É isso professor! Espero que o senhor tenha gostado.'''