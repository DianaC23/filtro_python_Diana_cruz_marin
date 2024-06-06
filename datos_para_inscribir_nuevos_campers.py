import json
def cargar_y_guardar(nuevo_datos):
    with open('datos.json', 'r') as file:
        datos = json.load(file)

    if isinstance(datos, dict):
        if "campers" in datos:
            datos["campers"]== nuevo_datos
        else:
            datos["campers"] = [nuevo_datos]
    elif isinstance(datos, list):
        datos.append(nuevo_datos)
    else:
        datos = [nuevo_datos]
    with open('datos.json', 'w') as file:
        json.dump(datos, file, indent=4)