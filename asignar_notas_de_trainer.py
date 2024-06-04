import guardar_nota_evaluada as evaluar
def asignar_las_notas_del_camper():
    while True:
        docu = input("Digite el documento del camper inscrito: ")
        new = evaluar.cargar_usuario()
        if (docu) in new["campers"]:
            print("Ingresar notas del camper")
            nota1 = int(input("Digite la primera nota"))
            nota2 = int(input("Digite la segunda nota"))
            nota3 = int(input("Digite la tercera nota"))
            nota_evaluar = (nota1 * 0.3)+(nota2 *  0.6) + (nota3 * 0.1)
            if nota_evaluar >60:
                new["campers"][str(docu)]["risk"] = "Aprobado"
                new["campers"][str(docu)]["notas_trainer"] = nota_evaluar
                print("El camper fue aprobado exitosamente :)")
                evaluar.guardar_evaluada(new)
            elif nota_evaluar <60:
                new["campers"][str(docu)]["risk"] = "Rendimiento bajo"
                new["campers"][str(docu)]["notas_trainer"] = nota_evaluar
                new["campers"][str(docu)]["llamado"] = 1
                print("El camper esta en rendimiento bajo :(")
                print("Tienes un llamado de atención muy pronto se comunicaran contigo")
                evaluar.guardar_evaluada(new)
            else:
                print("error")
        else:
            print("El camper no se encuentra en la base de datos")
            break