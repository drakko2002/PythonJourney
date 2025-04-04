import os
import shutil

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
exe_path = os.path.join(downloads_path, "Executable Files")

os.makedirs(exe_path, exist_ok=True)

for filename in os.listdir(downloads_path):
    if filename.lower().endswith(".exe") or filename.lower().endswith(".msi"):
        origem = os.path.join(downloads_path, filename)
        destino = os.path.join(exe_path, filename)


        try:
            shutil.move(origem,destino)
            print(f"O arquivo {filename} foi movido com sucesso para {origem}!")
        except Exception as e:
            print(f"Ocorreu um erro ao mover {filename} para {destino}: {e}")