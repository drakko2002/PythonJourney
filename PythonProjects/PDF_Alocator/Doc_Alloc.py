import os
import shutil

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
imagery_path = os.path.join(downloads_path, "Images")
#Nisso, buscamos o caminho de sistema dos downloads e
#definimos uma pasta para mover os arquivos de PDF

os.makedirs(imagery_path, exist_ok=True)
#Faz checagem do diretório com validação por valor booleano
#Para constatar se existe ou não.

for filename in os.listdir(downloads_path):
    if (filename.lower().endswith(".webp") or filename.lower().endswith(".jpeg") or filename.lower().endswith(".jpg") or
            filename.lower().endswith(".png")) or filename.lower().endswith(".gif"):
        origem = os.path.join(downloads_path, filename)
        destino = os.path.join(imagery_path, filename)
        #Laço for pra definição de variáveis e caminhos

        try:
            shutil.move(origem, destino)
            print(f"Movido com sucesso: {filename}")
        except Exception as e:
            print(f"Ocorreu um erro ao mover {filename}: {e}")
            #Bloco try/except pra tentativa com retorno de exceção
            #Salva na variável "e" para boas práticas.