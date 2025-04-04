import os
import shutil

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
ctengine = os.path.join(downloads_path, "CT Script Files")

os.makedirs(ctengine, exist_ok=True)

def cten():
    for filename in os.listdir(downloads_path):
        if filename.lower().endswith(".ct"):
            origem = os.path.join(downloads_path, filename)
            destino = os.path.join(ctengine, filename)


            try:
                shutil.move(origem,destino)
                print(f"O arquivo {filename} foi movido com sucesso para {origem}!")
            except Exception as e:
                print(f"Ocorreu um erro ao mover {filename} para {destino}: {e}")
cten()