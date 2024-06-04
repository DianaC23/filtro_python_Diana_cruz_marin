import json
def cargar_y_guardar(nuevo_datos):
    with open('datos.json', 'r') as file:
        datos = json.load(file)

    if isinstance(datos, dict):
        if "campers" in datos:
            datos["campers"].append(nuevo_datos)
        else:
            datos["campers"] = [nuevo_datos]
    elif isinstance(datos, list):
        datos.append(nuevo_datos)
    else:
        datos = [nuevo_datos]
    with open('datos.json', 'w') as file:
        json.dump(datos, file, indent=4) 

        
"""def cargar_y_guardar(nuevos_datos, nombre_archivo='datos.json'):
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = []

    datos.append(nuevos_datos)

    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)"""