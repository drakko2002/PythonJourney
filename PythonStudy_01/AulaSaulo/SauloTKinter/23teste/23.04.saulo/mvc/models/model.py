import sqlite3

class Model:
    def __init__(self):        
        '''
        Este método é chamado quando a classe Model é instanciada.
        Ele é responsável por criar a conexão com o banco de dados e criar a tabela clientes.

        O método connect() é usado para criar uma conexão com o banco de dados.
        O método cursor() é usado para criar um cursor, que é um objeto que permite executar comandos SQL.
        O método execute() é usado para executar um comando SQL.
        O método commit() é usado para salvar as alterações no banco de dados.
        '''
        self.db_connection = sqlite3.connect('agenda.db')
        cursor = self.db_connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                senha TEXT NOT NULL
            )
        ''')
        self.db_connection.commit()
        
    def cadastrar(self, nome: str, email: str, senha: str):
        '''

        Instale o SQLite Viewer para visualizar o banco de dados.
        O método Error é usado para tratar erros que podem ocorrer ao executar o comando SQL.
        Um exemplo de erro é quando o banco de dados não está conectado ou não existe. 
        Nestes casos, o método Error é chamado e retorna False.
        '''	
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''
                INSERT INTO clientes (nome, email, senha)
                VALUES (?, ?, ?)
            ''', (nome, email, senha))
            self.db_connection.commit()
            return True
        except sqlite3.Error:
            return False

    def eliminar(self, id: int):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('DELETE FROM clientes WHERE id = ?', (id,))
            self.db_connection.commit()
            return True
        except sqlite3.Error:
            return False

    def alterar(self, id: int, nome: str, email: str, senha: str) -> bool:
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('''
                UPDATE clientes 
                SET nome = ?, email = ?, senha = ?
                WHERE id = ?
            ''', (nome, email, senha, id))
            self.db_connection.commit()
            return True
        except sqlite3.Error:
            return False

    def listar(self) -> list:
        '''
        Este método é chamado quando o botão "Listar" é clicado e ele retorna uma lista de todos os clientes do banco de dados.
        Ele é responsável por listar todos os clientes do banco de dados.

        O método fetchall() é usado para obter todos os resultados da consulta SQL.
        '''
        try:
            cursor = self.db_connection.cursor()
            cursor.execute('SELECT * FROM clientes')
            return cursor.fetchall()
        except sqlite3.Error:
            return []



