import manejo_archivos
def asignar_salon():
    while True:
        datos = manejo_archivos.cargar_datos("datos.json")
        id_trainer = int(input("Elija un trainer para asignarle un area de trabajo\n (1)Juan,(2)Jholver,(3)Miguel"))
        if id_trainer == 1:
            salon = int(input("Elija uno de los salones (1)sputnik,(2)apolo,(3)artemis"))
            if salon == 1:
                datos["AREAS"]["aREA1"]["NAREA1"] = "Sputnik"
                datos["Tiempo"]["horario1"]["area"] = "Sputnik"
                datos["Tiempo"]["horario1"]["inicio"] = "10pm"
                datos["Tiempo"]["horario1"]["final"] = "2pm"
                datos["AREAS"]["aREA1"]["horai"] = "10 am"
                datos["AREAS"]["aREA1"]["horaf"] = "2pm"
                print("El salón de entrenamiento ha sido agregado exitosamente")
            elif salon == 2:
                datos["AREAS"]["aREA1"]["NAREA1"] = "Apolo"
                datos["Tiempo"]["horario1"]["area"] = "Apolo"
                datos["Tiempo"]["horario1"]["inicio"] = "10pm"
                datos["Tiempo"]["horario1"]["final"] = "2pm"
                datos["AREAS"]["aREA1"]["horai"] = "10 am"
                datos["AREAS"]["aREA1"]["horaf"] = "2pm"
                print("El salón de entrenamiento ha sido agregado exitosamente")
            elif salon == 3:
                datos["AREAS"]["aREA1"]["NAREA1"] = "Artemis"
                datos["Tiempo"]["horario1"]["area"] = "Artemis"
                datos["Tiempo"]["horario1"]["inicio"] = "10pm"
                datos["Tiempo"]["horario1"]["final"] = "2pm"
                datos["AREAS"]["aREA1"]["horai"] = "10 am"
                datos["AREAS"]["aREA1"]["horaf"] = "2pm"
                print("El salón de entrenamiento ha sido agregado exitosamente")
        elif id_trainer == 2:
            salon = int(input("Elija uno de los salones (1)sputnik,(2)apolo,(3)artemis"))
            if salon == 1:
                datos["AREAS"]["aREA2"]["NAREA2"] = "Sputnik"
                datos["Tiempo"]["horario1"]["area"] = "Sputnik"
                datos["Tiempo"]["horario2"]["inicio"] = "2pm"
                datos["Tiempo"]["horario2"]["final"] = "6pm"
                datos["AREAS"]["aREA2"]["horai"] = "2pm"
                datos["AREAS"]["aREA2"]["horaf"] = "6pm"
                print("El salón de entrenamiento ha sido agregado exitosamente")
            elif salon == 2:
                datos["AREAS"]["aREA2"]["NAREA2"] = "Apolo"
                datos["Tiempo"]["horario2"]["area"] = "Apolo"
                datos["Tiempo"]["horario2"]["inicio"] = "2pm"
                datos["Tiempo"]["horario2"]["final"] = "6pm"
                datos["AREAS"]["aREA2"]["horai"] = "2pm"
                datos["AREAS"]["aREA2"]["horaf"] = "6pm"
                print("El salón de entrenamiento ha sido agregado exitosamente")
            elif salon == 3:
                datos["AREAS"]["aREA2"]["NAREA2"] = "Artemis"
                datos["Tiempo"]["horario2"]["area"] = "Artemis"
                datos["Tiempo"]["horario2"]["inicio"] = "2pm"
                datos["Tiempo"]["horario2"]["final"] = "6pm"
                datos["AREAS"]["aREA2"]["horai"] = "2pm"
                datos["AREAS"]["aREA2"]["horaf"] = "6pm"
                print("El salón de entrenamiento ha sido agregado exitosamente")
        elif id_trainer == 3:
            salon = int(input("Elija uno de los salones (1)sputnik,(2)apolo,(3)artemis"))
            if salon == 1:
                datos["AREAS"]["aREA3"]["NAREA3"] = "Sputnik"
                datos["Tiempo"]["horario3"]["area"] = "Sputnik"
                datos["Tiempo"]["horario3"]["inicio"] = "6 am"
                datos["Tiempo"]["horario3"]["final"] = "10 am"
                datos["AREAS"]["aREA3"]["horai"] = "6 am"
                datos["AREAS"]["aREA3"]["horaf"] = "10 am"
                print("El salón de entrenamiento ha sido agregado exitosamente")
            elif salon == 2:
                datos["AREAS"]["aREA3"]["NAREA3"] = "Apolo"
                datos["Tiempo"]["horario3"]["area"] = "Apolo"
                datos["Tiempo"]["horario3"]["inicio"] = "6 am"
                datos["Tiempo"]["horario3"]["final"] = "10 am"
                datos["AREAS"]["aREA3"]["horai"] = "6 am"
                datos["AREAS"]["aREA3"]["horaf"] = "10 am"
                print("El salón de entrenamiento ha sido agregado exitosamente")
            elif salon == 3:
                datos["AREAS"]["aREA3"]["NAREA3"] = "Artemis"
                datos["Tiempo"]["horario3"]["area"] = "Artemis"
                datos["Tiempo"]["horario3"]["inicio"] = "6 am"
                datos["Tiempo"]["horario3"]["final"] = "10 am"
                datos["AREAS"]["aREA3"]["horai"] = "6 am"
                datos["AREAS"]["aREA3"]["horaf"] = "10 am"
                print("El salón de entrenamiento ha sido agregado exitosamente")
            else:
                print("error")
        else:
            print("error")
        
        manejo_archivos.guardar_datos("datos.json",datos)