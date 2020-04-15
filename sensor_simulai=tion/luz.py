import json
import random

opcao = ["ON", "OFF"]
luz = [random.choice(opcao) for i in range(1000)]
print(luz)

with open("luz.json", "w") as arq_json:
    json.dump(luz, arq_json)