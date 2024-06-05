import camper_in_area
def camper_a_areas():
    while True:
        camperarea = input("Ingrese el ID del estudiante")
        puesto = camper_in_area.guardar_el_camper()
        if camperarea in puesto["campers"]:
            if puesto["campers"][camperarea]["state"] == "aprobado":
                elegir = int(input("Elija el area de entrenamiento\n (1)para sputnik\n (2)para apolo\n (3)para artemis: "))
                if elegir == 1:
                    puesto["campers"][(camperarea)]["AREAS"] = "sputnik"
                    camper_in_area.guardar_el_camper(puesto[""])
                    print("El camper ha sido agregado exitosamente")
                elif elegir == 2:
                    puesto["campers"][(camperarea)]["AREAS"] = "apolo"
                    
                    print("El camper ha sido agregado exitosamente")
                elif elegir == 3:
                    puesto["campers"][(camperarea)]["AREAS"] = "artemis"

                    print("El camper ha sido agregado exitosamente")
                else:
                    print("error al tratar de ingresar el trabajo")
            else:
                print("El camper no puede entrar a un ara de entrnamiento porque no esta inscrito")

        else:
            print("El camper no se encuentra en la base de datos")
            break