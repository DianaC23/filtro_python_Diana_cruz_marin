import json
def guardaruta(rutas):
    with open('rutas.json','w')as file:
        json.dump(rutas,file, indent=4)
def cargar_usuario():
    try:
        with open('rutas.json','r')as file:
            rutas = json.load(file)
    except FileNotFoundError:
        rutas = {"rrutas":{}}
    except json.JSONDecoderError:
        rutas = {"rrutas":{}}
    return rutas
"""import json
def cargar_y_guardar_rutas(nuevo_rutas):
    with open('rutas.json', 'r') as file:
        datos = json.load(file)

    if isinstance(datos, dict):
        if "rrutass" in datos:
            datos["rrutas"].append(nuevo_rutas)
        else:
            datos["rrutas"] = [nuevo_rutas]
    elif isinstance(datos, list):
        datos.append(nuevo_rutas)
    else:
        datos = [nuevo_rutas]
    with open('rutas.json', 'w') as file:
        json.dump(datos, file, indent=4) """