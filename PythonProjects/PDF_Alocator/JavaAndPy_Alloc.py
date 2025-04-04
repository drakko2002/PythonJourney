import os
import shutil

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
provisory_path = os.path.join(downloads_path, "Programming Files")

os.makedirs(provisory_path, exist_ok=True)

def javapy():
    for filename in os.listdir(downloads_path):
        if filename.lower().endswith(".java") or filename.lower().endswith(".py"):
            origem = os.path.join(downloads_path, filename)
            destino = os.path.join(provisory_path, filename)


            try:
                shutil.move(origem,destino)
                print(f"O arquivo {filename} foi movido com sucesso para {origem}!")
            except Exception as e:
                print(f"Ocorreu um erro ao mover {filename} para {destino}: {e}")
javapy()