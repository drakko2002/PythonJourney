import tkinter as tk
from tkinter import ttk


class View:
    def __init__(self, root, controller):
        self.window = root
        self.controller = controller
        self.window.geometry("800x400")
        self.window.title("Aqui vai o nome de sua aplicação")

        # Configuração de estilos
        self.style = ttk.Style()
        self.style.configure('Cinza.TFrame', background='#4F4F4F')
        self.style.configure('BrancoTexto.TLabel', background='#4F4F4F', foreground='white')

        # Criar frames
        self._criar_frame_topo()
        self._criar_frame_principal()
        self._criar_frame_rodape()

    def _criar_frame_topo(self):
        self.top_frame = ttk.Frame(self.window, height=50, style='Cinza.TFrame')
        self.top_frame.pack(fill="x", padx=1, pady=1)
        self.top_frame.pack_propagate(False)

        # Configurar título diretamente
        self.title_label = ttk.Label(self.top_frame, text="Aqui vai uma mensagem de título.",
                                     font=("Helvetica", 16, "bold"), style='BrancoTexto.TLabel')
        self.title_label.place(x=20, y=10)

    def _criar_frame_principal(self):
        self.main_frame = ttk.Frame(self.window)
        self.main_frame.pack(padx=1, pady=1, fill="both", expand=True)

        self.label_nome = ttk.Label(self.main_frame, text="Nome")
        self.label_nome.place(x=20, y=50)

        self.edit_nome = ttk.Entry(self.main_frame)
        self.edit_nome.place(x=20, y=80)

        self.label_email = ttk.Label(self.main_frame, text="Email")
        self.label_email.place(x=20, y=120)

        self.edit_email = ttk.Entry(self.main_frame)
        self.edit_email.place(x=20, y=150)

        self.label_senha = ttk.Label(self.main_frame, text="Senha")
        self.label_senha.place(x=20, y=190)

        self.edit_senha = ttk.Entry(self.main_frame)
        self.edit_senha.place(x=20, y=210)

    def _criar_frame_rodape(self):
        '''
        Observe que essa solução permite que a propriedade command permaneça intacta,
        e ainda assim chamar o método cadastrar da classe controller.

        No exemplo anterior, o command estava fora da classe Button, o que dificultava seu entendimento.
        '''

        self.bottom_frame = ttk.Frame(self.window, height=50, style='Cinza.TFrame')
        self.bottom_frame.pack(fill="x", padx=1, pady=1, side="bottom")
        self.bottom_frame.pack_propagate(False)

        self.botao_cadastrar = ttk.Button(self.bottom_frame, text="Cadastrar", command=self.controller.cadastrar)
        self.botao_cadastrar.place(x=20, y=10)

        self.botao_eliminar = ttk.Button(self.bottom_frame, text="Eliminar", command=self.controller.eliminar)
        self.botao_eliminar.place(x=100, y=10)

        self.botao_alterar = ttk.Button(self.bottom_frame, text="Alterar", command=self.controller.alterar)
        self.botao_alterar.place(x=180, y=10)

        self.label_nome = ttk.Label(self.bottom_frame, text="Mensagem")
        self.label_nome.place(x=260, y=10)

    def get_dados_formulario(self):
        '''
        Este método é chamado quando o botão "Cadastrar" é clicado. O processo é o seguinte:

        1. Botão clicado na View.
        2. O método cadastrar da classe controller é chamado.
        3. O método cadastrar da classe controller chama o método get_dados_formulario() da classe View
        4. O método get_dados_formulario() da classe View retorna um dicionário com os dados dos campos do formulário
        5. O dicionário é passado como argumento para o método cadastrar da classe model.
        '''
        return {
            'nome': self.edit_nome.get(),
            'email': self.edit_email.get(),
            'senha': self.edit_senha.get()
        }

    def limpar_formulario(self):
        '''
        Este método é chamado quando o botão "Cadastrar" é clicado. O processo é o seguinte:        

        1. Botão é clicado na View.
        2. O método limpar_formulario() da classe View é chamado após o cadastro.
        3. O método limpar_formulario() da classe View limpa os campos do formulário.
        '''
        self.edit_nome.delete(0, tk.END)
        self.edit_email.delete(0, tk.END)
        self.edit_senha.delete(0, tk.END)
