import manejo_archivos
def trainers_encargado():
    while True:
        datos = manejo_archivos.cargar_datos("datos.json")
        
        """id_estudiante = input("Ingrese el ID del estudiante")

        if id_estudiante not in datos["campers"]:
            print ("El estudiante no se encuentra registrado")
            return

        if datos["campers"][id_estudiante]["state"] != "Aprobado":
            print("El estudiante debe estar aprobado para poder agregarse a un area")
            return"""

        elegir = int(input("Elija el trainer\n (1)Juan\n (2)para jholver\n (3)para miguel: "))
        if elegir == 1:
            if datos["Tiempo"]["horario1"]["inicio"] == "6am" and datos["Tiempo"]["horario1"]["final"] == "10am" and datos["Tiempo"]["horario3"]["inicio"] == "10am" and datos["Tiempo"]["horario3"]["final"] == "6pm":
                print("El profesor Juan no puede trabajar en este horario")
            else:
                elegirr = int(input("Elija la ruta\n (1)Node\n (2)Java\n (3)NetCore: "))
                if elegirr == 1:

                    datos["Rutas"]["ruta1"]["trainerescogido"]= "Juan"
                    print("Se ha asignado un trainer a la ruta")
                elif elegirr == 2:

                    datos["Rutas"]["ruta2"]["trainerescogido"]= "Juan"
                    print("Se ha asignado un trainer a la ruta")
                elif elegirr == 3:

                    datos["Rutas"]["ruta3"]["trainerescogido"]= "Juan"
                    print("Se ha asignado un trainer a la ruta")
                else:
                    print("error al tratar de ingresar el trabajo")
        elif elegir == 2:
            if datos["Tiempo"]["horario1"]["inicio"] == "6am" and datos["Tiempo"]["horario1"]["final"] == "10am" and datos["Tiempo"]["horario3"]["inicio"] == "10am" and datos["Tiempo"]["horario3"]["final"] == "2pm":
                print("El profesor Juan no puede trabajar en este horario")
            else:
                elegirr = int(input("Elija la ruta\n (1)Node\n (2)Java\n (3)NetCore: "))
                if elegirr == 1:

                    datos["Rutas"]["ruta1"]["trainerescogido"]= "Jholver"
                    print("Se ha asignado un trainer a la ruta")
                elif elegirr == 2:

                    datos["Rutas"]["ruta2"]["trainerescogido"]= "Jholver"
                    print("Se ha asignado un trainer a la ruta")
                elif elegirr == 3:

                    datos["Rutas"]["ruta3"]["trainerescogido"]= "Jholver"
                    print("Se ha asignado un trainer a la ruta")
                else:
                    print("error al tratar de ingresar el trabajo")
                
        elif elegir == 3:
            if datos["Tiempo"]["horario1"]["inicio"] == "10am" and datos["Tiempo"]["horario1"]["final"] == "1pm" and datos["Tiempo"]["horario3"]["inicio"] == "10am" and datos["Tiempo"]["horario3"]["final"] == "2pm":
                print("El profesor Juan no puede trabajar en este horario")
            else:
                elegirr = int(input("Elija la ruta\n (1)Node\n (2)Java\n (3)NetCore: "))
                if elegirr == 1:

                    datos["Rutas"]["ruta1"]["trainerescogido"] = "Miguel"
                    print("Se ha asignado un trainer a la ruta")
                elif elegirr == 2:

                    datos["Rutas"]["ruta2"]["trainerescogido"] = "Miguel"
                    print("Se ha asignado un trainer a la ruta")
                elif elegirr == 3:

                    datos["Rutas"]["ruta3"]["trainerescogido"] = "Miguel"
                    print("Se ha asignado un trainer a la ruta")
                else:
                    print("error al tratar de ingresar el trabajo")
        else:
            print("error")
        break
        
        manejo_archivos.guardar_datos("datos.json",datos)