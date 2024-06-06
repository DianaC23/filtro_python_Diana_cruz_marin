import asignar_notas_estudiantes_aprobados
import asignar_campers_a_areas
import asignar_trainer_encargados
import asignar_salon_entrenamiento
"""import json"""
def menu_coordinador_menu():
     while True:
        menu_cordinador = (
                        "¿Que te gustaria hacer?\n"
                        "Presiona \n"
                        "1 Quieres ver rutas de entrenamiento \n"
                        "2 Quieres registrar las notas de los campers\n"
                        "3 Quieres crear rutas de entrenamiento \n"
                        "4 Quieres asignar campers a rutas\n"
                        "5 Modulo de matricula\n"
                        "6 Consultar campers con bajo rendimiento\n"
                        "7 Modulo de reportes\n"
                        "8 para salir"    
                )                   
        print(menu_cordinador)
        opc_menu_coordinador = input("- ")      
                #1 para ver la rutas de entrenamiento
        if opc_menu_coordinador == "1":
                print("ver rutas de entrenamiento")
                print('rutas.json')
                    #2 para registrar las notas de los campers
        elif opc_menu_coordinador == "2":
             print("registrar las notas de los campers")
             asignar_notas_estudiantes_aprobados.leer_datos()
                #3 Quieres crear rutas de entrenamiento
        elif opc_menu_coordinador == "3":
                print("crear rutas de entrenamiento")       
            #4 para asignar campers a rutas de entrenamiento
        elif opc_menu_coordinador == "4":
                print("asignar campers a rutas de entrenamiento")
                asignar_campers_a_areas.camper_a_areas()
            #asignar trainers a rutas [33]
            #Modulo de matricula
        elif opc_menu_coordinador == "5":
                print("modulo de matricula")
                opc_modulo_asignar =(
                "1 asignar los campers aprobados\n"
                "2 asignar trainer encargado,asignar fecha de inicio,final  y asignar su ruta\n"
                "3 asignar salon de entrenamiento\n")
                "4 para salir"
                print(opc_modulo_asignar)
                opc_modul_asignar = input("- ")
                if opc_modul_asignar == "1":
                    print("asignar los campers aprobados")
                    asignar_campers_a_areas.camper_a_areas()
                elif opc_modul_asignar == "2":
                    print("asignar trainer encargado,asignar fecha de inicio y final  y asignar su ruta")
                    asignar_trainer_encargados.trainers_encargado()
                elif opc_modul_asignar == "3":
                    print("asignar salon de entrenamiento")
                    asignar_salon_entrenamiento.asignar_salon()
                elif opc_modul_asignar == "4":
                    print("Gracias por usar nuestro programa")
                    break
            #Consultar campers con bajo rendimiento
        elif opc_menu_coordinador == "6":
                print("consultar campers con bajo rendimiento")
            #8 Modulo de reportes
        elif opc_menu_coordinador == "7":
                print("modulo de reportes")  
                opc_modul_reportes = (
                "1 para Listar los campers que se encuentren en estado de inscrito.\n"
                "2 para Listar los campers que aprobaron el examen inicial.\n"
                "3 para Listar los entrenadores que se encuentran trabajando con CampusLands.\n"
                "4 para Listar los campers que cuentan con bajo rendimiento.\n"
                "5 para Listar los campers y trainers que se encuentren asociados a una ruta de entrenamiento.\n"
                "6 para Mostrar cuantos campers perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.\n"
                "7 para salir")
                print(opc_modul_reportes)
                opc_modul_reportes = input("- ")
                if opc_modul_reportes == "1":
                    print("Listar los campers que se encuentren en estado de inscrito.")
                    """campers_inscritos.inscritos()"""
                elif opc_modul_reportes == "2":
                    print("para Listar los campers que aprobaron el examen inicial.")
                elif opc_modul_reportes == "3":
                    print("para Listar los entrenadores que se encuentran trabajando con CampusLands.")
                elif opc_modul_reportes == "4":
                    print("para Listar los campers que cuentan con bajo rendimiento.")
                elif opc_modul_reportes == "5":
                    print("para Listar los campers y trainers que se encuentren asociados a una ruta de entrenamiento.")
                elif opc_modul_reportes == "6":
                    print("para Mostrar cuantos campers perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.")
                elif opc_modul_reportes == "7":
                    print("para salir")
                else:
                    print("error por favor ingrese uno de los valores que aparecen en pantalla")
            #para salir
        elif opc_menu_coordinador == "8":
                print("Gracias por usar nuestro programa")
                break
        else:
                print("error por favor ingrese uno de los valores que aparecen en pantalla")