import json
#mostrar inscritos
def mostrari():
    file = open ("datos.json")
    inscritos = json.load(file)
    for documento, datos in inscritos["campers"].items():
        print("El usuario",datos["name"],datos["last_name"], "con estado", datos["state"], documento )


#mostrar aprobados
def mostraraprobaroni():
    file = open ("datos.json")
    aprobados = json.load(file)
    for documento, datos in aprobados["campers"].items():
        print("El usuario",datos["name"],datos["last_name"], "con estado", datos["risk"], documento )
#mostrar entrenadores
def mostrarentrenadores():
    file = open ("datos.json")
    entrenadores = json.load(file)
    for documento, datos in entrenadores["Trainers"].items():
        print("los entrenadores son: ",datos["trainer1"],datos["trainer2"], "con estado", datos["trainer3"], documento )
#mostrar campers con bajo rendimiento
def mostrarbajo():
    file = open ("datos.json")
    bajo = json.load(file)
    for documento, datos in bajo["en_riesgo"].items():
        print("los campers son: ",datos["RIESGO_CAMPER"], documento)
#campers y trainers en una ruta  de entrenamiento
def mostrarasociadosaruta():
    file = open ("datos.json")
    bajo = json.load(file)
    for documento, datos in bajo["AREAS"].items():
        print("los campers son: ",datos["GUARDAR_CAMPER"], documento)
    
