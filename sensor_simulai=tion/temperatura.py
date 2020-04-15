import json
import random

val_sen = 1000
temperatura = [random.randint(0,50) for i in range(val_sen)]
print(temperatura)

with open("temperatura.json", "w") as arq_json:
    json.dump(temperatura, arq_json)
