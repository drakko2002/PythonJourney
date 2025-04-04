import os
import shutil

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
Zip_files = os.path.join(downloads_path, "Zip and Rar Files")

os.makedirs(Zip_files, exist_ok=True)

for filename in os.listdir(downloads_path):
    if filename.lower().endswith(".zip") or filename.lower().endswith(".rar") or filename.lower().endswith(".7z"):
        origem = os.path.join(downloads_path, filename)
        destino = os.path.join(Zip_files, filename)

        try:
            shutil.move(origem,destino)
            print(f"O arquivo comprimido {filename} foi movido com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao mover {filename}: {e}")
