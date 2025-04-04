import os
import shutil

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
sql_files = os.path.join(downloads_path, "sql Files")

os.makedirs(sql_files, exist_ok=True)

def sqfiles():
    for filename in os.listdir(downloads_path):
        if filename.lower().endswith(".sql"):
            origem = os.path.join(downloads_path, filename)
            destino = os.path.join(sql_files, filename)


            try:
                shutil.move(origem,destino)
                print(f"O arquivo {filename} foi movido com sucesso para {origem}!")
            except Exception as e:
                print(f"Ocorreu um erro ao mover {filename} para {destino}: {e}")


sqfiles()