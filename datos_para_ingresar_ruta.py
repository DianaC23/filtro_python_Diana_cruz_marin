import json
def cargar_y_guardar_new_ruta(RUTAS):
        with open('rutas.json', 'W') as file:
            json.dump(RUTAS, file , indent=4)
def cargar_y_guardar_nueva_ruta():
        try:
            with open('rutas.json', 'r') as g:
                  rutas = json.load(g)
                  return rutas
        except FileNotFoundError:
            print("Error al guardar")
            return{"Rutas":{}}
"""try:
        with open('rutas.son', 'r') as archivo:
            rutas = json.load(archivo)
    except FileNotFoundError:
        rutas = []

    rutas.append('rutas.json')

    with open('rutas.json', 'w') as archivo:
        json.dump(rutas, archivo, indent=4)"""
"""import json

def cargar_y_guardar_ruta(nuevas_datos, ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            rutas = json.load(archivo)
    except FileNotFoundError:
        rutas = []

    rutas.append(nuevas_datos)

    with open(ruta_archivo, 'a') as archivo:
        archivo.write(rutas, archivo, indent=4)
def leer_y_mostrar():
    with open('rutas.json', 'r') as file:
        rutas_dict = json.load(file)
    print(json.dumps(rutas_dict, indent=4))
#Trainer
def cargar_y_guardar_trainer(nuevas_datos, ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            trainers = json.load(archivo)
    except FileNotFoundError:
        trainers = []

    trainers.append(nuevas_datos)

    with open(ruta_archivo, 'a') as archivo:
        archivo.write(trainers, archivo, indent=4)
def leer_y_mostrar():
    with open('trainers.json', 'r') as file:
        rutas_dict = json.load(file)
    print(json.dumps(rutas_dict, indent=4))"""