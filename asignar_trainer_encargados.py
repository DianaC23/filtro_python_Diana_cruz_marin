import manejo_archivos
def trainers_encargado():
    while True:
        datos = manejo_archivos.cargar_datos("datos.json")  
        elegir = int(input("Elija el trainer\n (1)Juan\n (2)para jholver\n (3)para miguel: "))
        if elegir == 1:
            if datos["Tiempo"]["horario1"]["inicio"] == "6am" and datos["Tiempo"]["horario1"]["final"] == "10am" and datos["Tiempo"]["horario3"]["inicio"] == "10am" and datos["Tiempo"]["horario3"]["final"] == "6pm":
                print("El profesor Juan no puede trabajar en este horario")
            else:
                elegirr = int(input("Elija la ruta\n (1)Node\n (2)Java\n (3)NetCore: "))
                if elegirr == 1:

                    datos["Rutas"]["ruta1"]["trainerescogido"]= "Juan"
                    datos["Trainers"]["trainer1"]["Rutas"]= "NodeJS"
                    #Fecha de inicio
                    datos["Tiempo"]["horario2"]["inicio"]= "10am"
                    #fecha final
                    datos["Tiempo"]["horario2"]["final"]= "2pm"
                    print("Se ha asignado al trainer a Juan")
                    print("Se ha asignado la ruta de NodeJS")
                    print("La hora de inicio es a las 10am")
                    print("La hora de finalización es a las 2pm")
                elif elegirr == 2:

                    datos["Rutas"]["ruta2"]["trainerescogido"]= "Juan"
                    datos["Trainers"]["trainer1"]["Rutas"]= "Java"
                    #Fecha de inicio
                    datos["Tiempo"]["horario2"]["inicio"]= "10am"
                    #fecha final
                    datos["Tiempo"]["horario2"]["final"]= "2pm"
                    print("Se ha asignado al trainer a Juan")
                    print("Se ha asignado la ruta de Java")
                    print("La hora de inicio es a las 10am")
                    print("La hora de finalización es a las 2pm")
                elif elegirr == 3:

                    datos["Rutas"]["ruta3"]["trainerescogido"]= "Juan"
                    datos["Trainers"]["trainer1"]["Rutas"]= "NetCore"
                    #Fecha de inicio
                    datos["Tiempo"]["horario2"]["inicio"]= "10am"
                    #fecha final
                    datos["Tiempo"]["horario2"]["final"]= "2pm"
                    print("Se ha asignado al trainer a Juan")
                    print("Se ha asignado la ruta de NodeJS")
                    print("La hora de inicio es a las 10am")
                    print("La hora de finalización es a las 2pm")
                else:
                    print("error al tratar de ingresar el trabajo")
        elif elegir == 2:
            if datos["Tiempo"]["horario1"]["inicio"] == "6am" and datos["Tiempo"]["horario1"]["final"] == "10am" and datos["Tiempo"]["horario3"]["inicio"] == "10am" and datos["Tiempo"]["horario3"]["final"] == "2pm":
                print("El profesor Juan no puede trabajar en este horario")
            else:
                elegirr = int(input("Elija la ruta\n (1)Node\n (2)Java\n (3)NetCore: "))
                if elegirr == 1:

                    datos["Rutas"]["ruta1"]["trainerescogido"]= "Jholver"
                    datos["Trainers"]["trainer2"]["Rutas"]= "NodeJS"
                    #Fecha de inicio
                    datos["Tiempo"]["horario2"]["inicio"]= "2pm"
                    #fecha final
                    datos["Tiempo"]["horario2"]["final"]= "6pm"
                    print("Se ha asignado al trainer a Jholver")
                    print("Se ha asignado la ruta de NodeJS")
                    print("La hora de inicio es a las 2pm")
                    print("La hora de finalización es a las 6pm")
                elif elegirr == 2:

                    datos["Rutas"]["ruta2"]["trainerescogido"]= "Jholver"
                    datos["Trainers"]["trainer2"]["Rutas"]= "Java"
                    #Fecha de inicio
                    datos["Tiempo"]["horario2"]["inicio"]= "2pm"
                    #fecha final
                    datos["Tiempo"]["horario2"]["final"]= "6pm"
                    print("Se ha asignado al trainer a Jholver")
                    print("Se ha asignado la ruta de Java")
                    print("La hora de inicio es a las 2pm")
                    print("La hora de finalización es a las 6pm")
                elif elegirr == 3:

                    datos["Rutas"]["ruta3"]["trainerescogido"]= "Jholver"
                    datos["Trainers"]["trainer2"]["Rutas"]= "NetCore"
                    #Fecha de inicio
                    datos["Tiempo"]["horario2"]["inicio"]= "2pm"
                    #fecha final
                    datos["Tiempo"]["horario2"]["final"]= "6pm"
                    print("Se ha asignado al trainer a Jholver")
                    print("Se ha asignado la ruta de NetCore")
                    print("La hora de inicio es a las 2pm")
                    print("La hora de finalización es a las 6pm")
                else:
                    print("error al tratar de ingresar el trabajo")
                
        elif elegir == 3:
            if datos["Tiempo"]["horario1"]["inicio"] == "10am" and datos["Tiempo"]["horario1"]["final"] == "1pm" and datos["Tiempo"]["horario3"]["inicio"] == "10am" and datos["Tiempo"]["horario3"]["final"] == "2pm":
                print("El profesor Juan no puede trabajar en este horario")
            else:
                elegirr = int(input("Elija la ruta\n (1)Node\n (2)Java\n (3)NetCore: "))
                if elegirr == 1:

                    datos["Rutas"]["ruta1"]["trainerescogido"] = "Miguel"
                    datos["Trainers"]["trainer3"]["Rutas"]= "NodeJS"
                    #Fecha de inicio
                    datos["Tiempo"]["horario2"]["inicio"]= "6am"
                    #fecha final
                    datos["Tiempo"]["horario2"]["final"]= "10am"
                    print("Se ha asignado al trainer a Miguel")
                    print("Se ha asignado la ruta de NodeJS")
                    print("La hora de inicio es a las 6am")
                    print("La hora de finalización es a las 10am")
                elif elegirr == 2:

                    datos["Rutas"]["ruta2"]["trainerescogido"] = "Miguel"
                    datos["Trainers"]["trainer3"]["Rutas"]= "Java"
                    #Fecha de inicio
                    datos["Tiempo"]["horario2"]["inicio"]= "6am"
                    #fecha final
                    datos["Tiempo"]["horario2"]["final"]= "10am"
                    print("Se ha asignado al trainer a Miguel")
                    print("Se ha asignado la ruta de Java")
                    print("La hora de inicio es a las 6am")
                    print("La hora de finalización es a las 10am")
                elif elegirr == 3:

                    datos["Rutas"]["ruta3"]["trainerescogido"] = "Miguel"
                    datos["Trainers"]["trainer3"]["Rutas"]= "Netcore"
                    #Fecha de inicio
                    datos["Tiempo"]["horario2"]["inicio"]= "6am"
                    #fecha final
                    datos["Tiempo"]["horario2"]["final"]= "10am"
                    print("Se ha asignado al trainer a Miguel")
                    print("Se ha asignado la ruta de Netcore")
                    print("La hora de inicio es a las 6am")
                    print("La hora de finalización es a las 10am")
                else:
                    print("error al tratar de ingresar el trabajo")
        else:
            print("error")
        break
        
    manejo_archivos.guardar_datos("datos.json",datos)