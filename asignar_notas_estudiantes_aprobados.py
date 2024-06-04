import guardar_muestra
def leer_datos():
    while True:
        documento = input("Digite el documento del camper inscrito: ")
        nuevo = guardar_muestra.cargar_usuario()
        if (documento) in nuevo["campers"]:
            print("Ingresar notas del camper")
            nota1 = int(input("Digite la primera nota"))
            nota2 = int(input("Digite la segunda nota"))
            nota3 = int(input("Digite la tercera nota"))
            nota_final = (nota1 * 0.3)+(nota2 *  0.6) + (nota3 * 0.1)
            if nota_final >=60:
                nuevo["campers"][str(documento)]["state"] = "Aprobado"
                nuevo["campers"][str(documento)]["notas"] = nota_final
                print("El camper fue aprobado exitosamente :)")
                guardar_muestra.guardarusuario(nuevo)
            elif nota_final <60:
                nuevo["campers"][str(documento)]["state"] = "Reprobo"
                nuevo["campers"][str(documento)]["notas"] = nota_final
                print("El camper fue Reprobado :(")
                guardar_muestra.guardarusuario(nuevo)
            else:
                print("error")
        else:
            print("El camper no se encuentra en la base de datos")
            break    