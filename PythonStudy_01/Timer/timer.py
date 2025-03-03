import time
import sys

for i in range(15):
    contador = (15 - 1)
    print(f'Contagem: {contador}', end='\r', flush=True)
    time.sleep(1)

print("Fim")
