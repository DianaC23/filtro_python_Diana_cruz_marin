import manejo_archivos
def asignar_las_notas_del_camper():
    while True:       
        elejir = input("Digite el documento del camper inscrito: ")
        datos = manejo_archivos.cargar_datos("datos.json")
        if elejir in datos["campers"]:
            print("Ingresar notas del camper")
            nota1 = int(input("Digite la primera nota"))
            nota2 = int(input("Digite la segunda nota"))
            nota3 = int(input("Digite la tercera nota"))
            nota_evaluar = (nota1 * 0.3)+(nota2 *  0.6) + (nota3 * 0.1)
            if nota_evaluar >60:
                datos["campers"][str(elejir)]["risk"] = "Aprobado"
                datos["campers"][str(elejir)]["notas_trainer"] = nota_evaluar
                print("El camper fue aprobado exitosamente :)")
                manejo_archivos.guardar_datos("datos.json",datos)
            elif nota_evaluar <60:
                datos["campers"][str(elejir)]["risk"] = "Rendimiento bajo"
                datos["campers"][str(elejir)]["notas_trainer"] = nota_evaluar
                datos["campers"][str(elejir)]["llamado"] = 1

                datos["en_riesgo"]["RIESGO_CAMPER"].append(elejir)
                print("El camper esta en rendimiento bajo :(")
                print("Tienes un llamado de atención muy pronto se comunicaran contigo")
                manejo_archivos.guardar_datos("datos.json",datos)
            else:
                print("error")
        else:
            print("El camper no se encuentra en la base de datos")
            break
    manejo_archivos.guardar_datos("datos.json",datos)