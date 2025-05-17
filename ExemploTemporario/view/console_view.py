class ProdutorConsumidorView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Produtor-Consumidor MVC")
        self.geometry("600x400")

        # Frame de saída
        frame = ttk.Frame(self, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        # Lista de produção
        self.lst_produzidos = tk.Listbox(frame, height=10)
        self.lst_produzidos.grid(row=0, column=0, padx=5, pady=5, sticky=tk.NSEW)

        # Lista de consumo
        self.lst_consumidos = tk.Listbox(frame, height=10)
        self.lst_consumidos.grid(row=0, column=1, padx=5, pady=5, sticky=tk.NSEW)

        # Botões
        btn_frame = ttk.Frame(self, padding=10)
        btn_frame.pack(fill=tk.X)
        self.btn_start = ttk.Button(btn_frame, text="Iniciar")
        self.btn_start.pack(side=tk.LEFT, padx=5)
        self.btn_stop = ttk.Button(btn_frame, text="Parar", state=tk.DISABLED)
        self.btn_stop.pack(side=tk.LEFT, padx=5)

        # Configura grid
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

    def bind_start(self, callback):
        self.btn_start.config(command=callback)

    def bind_stop(self, callback):
        self.btn_stop.config(command=callback)

    def adicionar_producao(self, item, produtor):
        self.lst_produzidos.insert(tk.END, f"{produtor}: {item}")

    def adicionar_consumo(self, item, consumidor):
        self.lst_consumidos.insert(tk.END, f"{consumidor}: {item}")

    def on_started(self):
        self.btn_start.config(state=tk.DISABLED)
        self.btn_stop.config(state=tk.NORMAL)

    def on_stopped(self):
        self.btn_start.config(state=tk.NORMAL)
        self.btn_stop.config(state=tk.DISABLED)
