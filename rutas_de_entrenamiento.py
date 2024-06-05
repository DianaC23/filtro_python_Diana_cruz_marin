import datos_para_ingresar_ruta
def agregar_nuevas_rutas():
        nuevas_rutas = {}
        ruta = nuevas_rutas ["RUTAS"] = input("Ingrese la nueva ruta")
        nuevas_rutas["ruta"] = ruta
        print(nuevas_rutas)
        datos_para_ingresar_ruta.cargar_y_guardar_new_ruta()
        print("La ruta ha sido agregado exitosamente")
