
import json
import random

val_sen = 1000
opcao = ["Amarelo", "Vermelho", "Verde"]
luz = {}
for i in range(1000):
    id = i
    decisao = random.choice(opcao)
    if decisao == "Vermelho":
        alerta = "Alerta!"
    elif decisao == "Amarelo":
        alerta = "Cuidado"
    else:
        alerta = "Ok"
    luz[id] = [decisao, alerta]

print(luz)

with open("luz_ver2.json", "w") as arq_json:
    json.dump(luz, arq_json)
