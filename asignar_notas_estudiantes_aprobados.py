import json

import guardar_muestra
def leer_datos():
    while True:
        documento = input("Digite el documento del camper inscrito: ")#ponerle el int
        nuevo = guardar_muestra.guardarusuario(documento)
        if str(documento) in nuevo["campers"]:
            print("Ingresar notas del camper")
            
            nota1 = int(input("Digite la primera nota"))
            nota2 = int(input("Digite la segunda nota"))
            nota3 = int(input("Digite la tercera nota"))
            nota_final = (nota1 * 0.3)+(nota2 *  0.6) + (nota3 * 0.1)
            if nota_final >=60:
                nuevo["campers"][str(documento)]["state"] = "Aprobado"
                print("El camper fue aprobado exitosamente :)")
                guardar_muestra.guardar_usuario(nuevo)
            elif nota_final <60:
                nuevo["campers"][str(documento)]["state"] = "Reprobo"
                print("El camper fue aReprobado :(")
                guardar_muestra.guardar_usuario(nuevo)
            else:
                print("error")
        else:
            print("El camper no se encuentra en la base de datos")         
"""def leer_datos():
        with open('datos.json', 'r') as file:
            datos = json.load(file)
        return datos
    def guardar_datos(datos):
        with open('datos.json', 'w') as file:
            json.dump(datos, file, indent=4)
    def buscar_estudiante_por_id(datos, n_id):
        for estudiante in datos:
            if estudiante["N_ID"] == int(n_id):
                return estudiante
        return None
    datos = leer_datos()
    n_id = input("Ingrese el ID del estudiante: ")
    estudiante = buscar_estudiante_por_id(datos, n_id)
    print(estudiante)
    if estudiante:
        print("Ingrese notas del estudiante: ")
        nota1 = int(input("Ingrese la nota 1: "))
        nota2 = int(input("Ingrese la nota 2: "))
        nota3= int(input("Ingrese la nota 3: "))
        nota_final = (nota1 * 0.3) + (nota2 * 0.6) + (nota3 * 0.1)
        print("Nota final")
        estudiante["notas"] = nota_final
        guardar_datos(datos)
    else:
        print("El estudiante no se encuentra en la base de datos")"""