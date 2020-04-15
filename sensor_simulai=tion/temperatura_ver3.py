import json
import random
import time

x = 0
val_sen = 1000
temperatura = {}

while x != val_sen:
        valor = random.randint(0, 50)
        if valor > 30:
            condicao = "Alto"
        else:
            condicao = "Baixo"
        valor_temp = str(valor) + " " + "C"
        temperatura[x] = [valor_temp, condicao]
        print(temperatura[x])
        x = x + 1
        time.sleep(1)
with open("temperatura_ver3.json", "w") as arq_json:
    json.dump(temperatura, arq_json)