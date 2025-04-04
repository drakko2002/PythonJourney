import os
import shutil

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
mp4_path = os.path.join(downloads_path, "Arquivos de Áudio e Vídeo")

in_file = "5.1"

os.makedirs(mp4_path, exist_ok=True)


def mp4():
    for filename in os.listdir(downloads_path):
        if (filename.lower().endswith(".mp4") or filename.lower().endswith(".m4a")
                or filename.lower().endswith(".webm") or filename.lower().endswith("5.1") or '5.1' in filename)\
                or "720p" in filename.lower() or "1080p" in filename.lower():
            origem = os.path.join(downloads_path, filename)
            destino = os.path.join(mp4_path, filename)

            try:
                shutil.move(origem, destino)
                print(f"O arquivo {filename} foi movido para {destino}")
            except Exception as e:
                print(f"Ocorreu um erro ao mover o arquivo {filename}: {e}")
mp4()