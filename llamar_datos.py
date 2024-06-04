import json
def llamar ():
    while True:
        do = input("Digite el documento del camper inscrito: ")
        if do == ["n_ID"]:
            with open("datos.json","r") as file:
                data = json.load(file)
                if do in data["n_ID"]:
                    print("El usuario esta inscrito")
        else:
            print("No se encuentra en la lista de campers")
            #Organizar que solo devuelve que no esta inscrito pero si lo esta