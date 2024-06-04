import rutas_de_entrenamiento
def ingresar_datos_d_rutas():
    nuevas_rutas = {}
    n_ruta = nuevas_rutas ["n_ruta"]= input("Ingrese la nueva ruta: ")
    rut = {n_ruta:nuevas_rutas}
    print(rut)
    rutas_de_entrenamiento.agregar_nuevas_rutas(rut)
    print("La ruta ha sido agregado exitosamente")