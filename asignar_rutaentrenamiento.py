import manejo_archivos
def asignar_ruta():
    while True:
        datos = manejo_archivos.cargar_datos("datos.json")
        id_trainer = input("Ingrese el trainer")

        if id_trainer not in datos["Trainer"]:
            print ("El trainer no se encuentra registrado")
            return

        if datos["Trainers"]["trainer1"]["profe"] != "Juan" and datos["Trainers"]["trainer2"]["profe"] != "Jholver" and datos["Trainers"]["trainer3"]["profe"] != "Miguel":
            print("El trainer no se encuentra registrado")
            return

        elegir = int(input("Elija el area de entrenamiento\n (1)para sputnik\n (2)para apolo\n (3)para artemis: "))
        #Profesor use este que esta lo deje en cero para probar que no se puede llenar
        if elegir == 1:
            #Probar este que esta en cero para probar que no se puede llenar
            if datos["AREAS"]["aREA1"]["cantidad"] == 0:
                print("esta lleno no puedes meter mas")
            else:
                datos["AREAS"]["aREA1"]["GUARDAR_CAMPER"].append(id_estudiante)
                datos["AREAS"]["aREA1"]["cantidad"] -=1

                print("El camper ha sido agregado exitosamente")
        elif elegir == 2:
            if datos["AREAS"]["aREA1"]["cantidad"] == 0:
                print("esta lleno no puedes meter mas")
            else:
                datos["AREAS"]["aREA2"]["GUARDAR_CAMPER"].append(id_estudiante)
                datos["AREAS"]["aREA1"]["cantidad"] -=1
            print("El camper ha sido agregado exitosamente")
        elif elegir == 3:
            if datos["AREAS"]["aREA1"]["cantidad"] == 0:
                print("esta lleno no puedes meter mas")
            else:
                datos["AREAS"]["aREA3"]["GUARDAR_CAMPER"].append(id_estudiante)
                datos["AREAS"]["aREA1"]["cantidad"] -=1
            print("El camper ha sido agregado exitosamente")
        else:
            print("error al tratar de ingresar el trabajo")
        
        manejo_archivos.guardar_datos("datos.json",datos)   