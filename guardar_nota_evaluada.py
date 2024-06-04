import json
def guardar_evaluada(datos):
    with open('datos.json','w')as file:
        json.dump(datos,file,indent=4)
def cargar_usuario():
    try:
        with open('datos.json','r')as file:
            datos = json.load(file)
    except FileNotFoundError:
        datos = {"campers":{}}
    except json.JSONDecoderError:
        datos = {"campers":{}}
    return datos