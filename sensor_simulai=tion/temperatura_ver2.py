import json
import random
import time

def tempo():
    time.sleep(5)


val_sen = 1000
temperatura = {}
for i in range(1000):
    id = i
    valor = random.randint(0,50)
    if valor > 30:
        condicao = "Alto"
    else:
        condicao = "Baixo"
    valor_temp = str(valor)+" "+"C"
    temperatura[id] = [valor_temp, condicao]
print(temperatura)

with open("temperatura_ver2.json", "w") as arq_json:
    json.dump(temperatura, arq_json)


