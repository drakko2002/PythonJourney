import os
import shutil

downloads_path = os.path.join(os.path.expanduser('~'),"Downloads")
doc_path = os.path.join(downloads_path, "Doc Types")
#A variável downloads_path serve para obter por méthodo join o caminho do usuário do sistema
#E com isso feito, prossegue para a pasta downloads.

os.makedirs(doc_path, exist_ok=True)
#A biblioteca "os" também consegue criar pastas e aqui ela verifica com uma variável booleana se a pasta já
#existe!
def doc():
    for filename in os.listdir(downloads_path):
        #Aqui criamos um laço for que vai iterar pelos documentos contidos na lista de diretório
        #inserido como argumento.
        if filename.lower().endswith(".docx") or filename.lower().endswith(".pdf") or filename.lower().endswith(".ppt")\
                or filename.lower().endswith(".pptx") or filename.lower().endswith(".doc") or filename.lower().endswith(".rtf"):
            origem = os.path.join(downloads_path, filename)
            destino = os.path.join(doc_path, filename)


            try:
                shutil.move(origem, destino)
                print(f"O arquivo {filename} foi movido com sucesso para {destino}")
                #Bloco try tenta usar as variáveis origem e destino para mover os arquivos
                #E essa é exatamente a utilidade da biblioteca shutil com o method move!
            except Exception as e:
                print(f"Ocorreu um erro ao mover {filename} para {destino}: {e}")
doc()