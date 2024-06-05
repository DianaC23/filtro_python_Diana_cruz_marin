import json
def guardar_el_camper(elejir):
    with open('datos.json','w')as file:
        json.dump(elejir,file,indent=4)
def cargar_al_camper():
    try:
        with open('datos.json','r')as file:
            elejir = json.load(file)
    except FileNotFoundError:
        elejir = {"AREAS":{}}
    except json.decoder.JSONDecodeError:
        elejir = {"AREAS":{}}
    return elejir
