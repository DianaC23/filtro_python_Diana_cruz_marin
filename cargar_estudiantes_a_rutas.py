
"""import json
import random
def organizar_al_azar():
    #cargar ruta
    with open('ruta.json','r') as archivo:
        datos = json.load(archivo)
        print(datos)
    #cargar trainer
    with open('trainer.json','r') as archivo:
        datos = json.load(archivo)
        print(datos)
    #cargar campers
    with open('campers.json','r') as archivo:
        datos = json.load(archivo)
        print(datos)
    #asignar ruta a campers
    for camper in datos:
        camper["ruta"] = random.choice(datos)
    #asignar trainer a campers
    for camper in datos:
        camper["trainer"] = random.choice(datos)
    #asignar fecha de inicio a campers"""