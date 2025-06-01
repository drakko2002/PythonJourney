import os
import shutil

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
pdfs_path = os.path.join(downloads_path,"Scrap")
#Nisso, buscamos o caminho de sistema dos downloads e
#definimos uma pasta para mover os arquivos de PDF

os.makedirs(pdfs_path, exist_ok=True)
#Faz checagem do diretório com validação por valor booleano
#Para constatar se existe ou não.
def scrap():
    for filename in os.listdir(downloads_path):
        if filename.lower().endswith(".xlsx") or filename.lower().endswith(".htm")\
                or filename.lower().endswith(".html") or filename.lower().endswith(".mhtml")\
                or filename.lower().endswith(".xml") or filename.lower().endswith(".dll")\
                or filename.lower().endswith(".dat") or filename.lower().endswith(".htm")\
                or filename.lower().endswith(".jar"):
            origem = os.path.join(downloads_path, filename)
            destino = os.path.join(pdfs_path, filename)
            #Laço for pra definição de variáveis e caminhos

            try:
                shutil.move(origem, destino)
                print(f"Movido com sucesso: {filename}")
            except Exception as e:
                print(f"Ocorreu um erro ao mover {filename}: {e}")
                #Bloco try/except pra tentativa com retorno de exceção
                #Salva na variável "e" para boas práticas.
scrap()