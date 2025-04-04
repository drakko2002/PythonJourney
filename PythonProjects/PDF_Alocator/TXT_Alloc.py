import os
import shutil

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
text_files = os.path.join(downloads_path, "TXT Files")

os.makedirs(text_files, exist_ok=True)

def txt():
    for filename in os.listdir(downloads_path):
        if filename.lower().endswith(".txt"):
            origem = os.path.join(downloads_path, filename)
            destino = os.path.join(text_files, filename)


            try:
                shutil.move(origem,destino)
                print(f"O arquivo {filename} foi movido com sucesso para {destino}!")
            except Exception as e:
                print(f"Ocorreu um erro ao mover {filename} para {destino}: {e}")


txt()