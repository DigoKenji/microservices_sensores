import json
import random
import time

botao = False
val_sen = 1000
x = 0
fix = 10
varr = 10
temperatura = {}


def sensor(x, fix):
    while x != fix:
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


while not botao:
    op = raw_input("Digite a letra s para iniciar o sensor: ").upper()
    if op == "SAIR":
        botao = True
    else:
        sensor(x, fix)
        with open("temperatura_ver4.json", "w") as arq_json:
            json.dump(temperatura, arq_json)
        fix = fix + varr
        x = x + varr
