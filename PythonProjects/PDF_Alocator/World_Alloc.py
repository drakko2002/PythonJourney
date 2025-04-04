import os
import shutil

downloads_path = os.path.join(os.path.expanduser("~"),"Downloads")
wld_path = os.path.join(downloads_path, "Terraria Worlds")

os.makedirs(wld_path, exist_ok=True)

for filename in os.listdir(downloads_path):
    #Não pode esquecer de inserir downloads_path como argumento da função laço for!
    if filename.lower().endswith(".wld"):
        origem = os.path.join(downloads_path, filename)
        destino = os.path.join(wld_path, filename)

        try:
            shutil.move(origem, destino)
            print(f"O arquivo de mundo {filename} foi movido com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro {e} ao mover {filename}")