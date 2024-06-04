import datos_para_ingresar_ruta
def agregar_nuevas_rutas():
        nuevas_rutas = {}
        ruta = nuevas_rutas ["RUTAS"] = input("Ingrese la nueva ruta")
        nuevas_rutas["ruta"] = ruta
        print(nuevas_rutas)
        datos_para_ingresar_ruta.cargar_y_guardar_new_ruta()
        print("La ruta ha sido agregado exitosamente")
"""with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)"""
"""rrutas = guardar_rutas
 datos_rutas = {}
        n_ruta =datos_rutas ["n_ruta"]= input("Ingrese la ruta: ")
        rrutas = {n_ruta:datos_rutas}
        print(rrutas)
        guardar_rutas.guardaruta()
        print("La ruta se  ha sido agregado exitosamente")"""