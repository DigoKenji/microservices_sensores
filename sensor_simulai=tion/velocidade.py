import json
import random
import time

botao = False
val_sen = 1000
x = 0
fix = 10
varr = 10
velocidade = {}


def sensor(x, fix):
    while x != fix:
        valor = random.randint(10, 55)
        if valor >= 40:
            condicao = "Alto"
        elif valor >= 20:
            condicao = "Medio"
        else:
            condicao = "Baixo"
        valor_vel = str(valor) + "m/s"
        velocidade[x] = [valor_vel, condicao]
        print(velocidade[x])
        x = x + 1
        time.sleep(1)


while not botao:
    op = raw_input("Digite a letra s para iniciar o sensor: ").upper()
    if op == "SAIR":
        botao = True
    else:
        sensor(x, fix)
        with open("velocidade.json", "w") as arq_json:
            json.dump(velocidade, arq_json)
        fix = fix + varr
        x = x + varr