import json
import random
import time

botao = False
val_sen = 1000
x = 0
fix = 10
varr = 10
luz = {}
opcao = ["Amarelo", "Vermelho", "Verde"]


def sensor_luz(x, fix):
    while x != fix:
        decisao = random.choice(opcao)
        if decisao == "Vermelho":
            alerta = "Alerta!"
        elif decisao == "Amarelo":
            alerta = "Cuidado"
        else:
            alerta = "Ok"
        luz[x] = [decisao, alerta]
        print(luz[x])
        x = x + 1
        time.sleep(1)


while not botao:
    op = raw_input("Digite a letra s para iniciar o sensor: ").upper()
    if op == "SAIR":
        botao = True
    else:
        sensor_luz(x, fix)
        with open("luz_ver3.json", "w") as arq_json:
            json.dump(luz, arq_json)
        fix = fix + varr
        x = x + varr
