import json
#Funcion de cargar datos
def cargar_datos(nombre_archivo):
    try:
        with open(nombre_archivo,"r", encoding="utf-8") as file:
            print("datos cargados correctamente")
            return json.load(file)
    except Exception :
        print("error al cargar los datos")
#funcion de guardar datos
def guardar_datos(nombre_archivo,data):
    try:
        with open(nombre_archivo,"w", encoding="utf-8") as file:
            json.dump(data, file, indent=4,ensure_ascii=False)
            print("guardo correctamente")
    except Exception:
        print("error al guardar los datos")
#Listar los campers que se encuentran inscritos
