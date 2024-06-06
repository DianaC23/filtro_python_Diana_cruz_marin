import json
def mostrari():
    file = open ("datos.json")
    inscritos = json.load(file)
    for documento, datos in inscritos["campers"].items():
        print("El usuario",datos["name"],datos["last_name"], "con estado", datos["state"], documento )

print(mostrari())