import datos_para_inscribir_nuevos_campers
def ingresar_datos_d_camper():
    datos_camper = {}
    datos_camper ["notas"] = 0
    datos_camper ["state"] = "inscrito"
    datos_camper ["risk"] = "en espera"
    datos_camper ["name"] = input("Ingrese su nombre: ")
    datos_camper ["last_name"] = input("Ingrese su apellido: ")
    datos_camper ["address"] = input("Ingrese su direccion: ")
    datos_camper ["acudiente"] = input("Ingrese su acudiente: ")
    datos_camper ["email"] = input("Ingrese su correo electronico: ")
    n_ID = datos_camper ["n_ID"]= int(input("Ingrese el numero de identificacion: "))
    datos_camper ["cell_phone"] = int(input("Ingrese su numero de celular: "))  
    datos_camper ["phone"] = int(input("Ingrese su numero de telefono: "))
    campers = {n_ID:datos_camper}
    print(campers)
    datos_para_inscribir_nuevos_campers.cargar_y_guardar(campers)
    print("El camper ha sido agregado exitosamente")
ingresar_datos_d_camper()