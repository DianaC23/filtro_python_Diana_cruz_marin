import manejo_archivos
def camper_a_areas():
    while True:
        datos = manejo_archivos.cargar_datos("datos.json")
        id_estudiante = input("Ingrese el ID del estudiante")

        if id_estudiante not in datos["campers"]:
            print ("El estudiante no se encuentra registrado")
            return

        if datos["campers"][id_estudiante]["state"] != "Aprobado":
            print("El estudiante debe estar aprobado para poder agregarse a un area")
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