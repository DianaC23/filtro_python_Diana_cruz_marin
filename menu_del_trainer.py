import asignar_notas_de_trainer
def menu_del_trainer_menu():
    opc_menu_trainer = (
    "1 Para ver tu ruta asignada\n"
    "2 Para ver su hora asignada\n"
    "3 Para poner notas a estudiantes\n"
    "4 Para ver el area de entrenamiento asignado\n"
    "5 Para salir"
        )
    print(opc_menu_trainer)
    opc_menu_triner = input("- ")
    if opc_menu_triner == "1":
        print("ver rutas de entrenamiento")
    elif opc_menu_triner == "2":
        print("ver hora asignada")
    elif opc_menu_triner == "3":
        print("poner notas a estudiantes")
        asignar_notas_de_trainer.asignar_las_notas_del_camper()
    elif opc_menu_triner == "4":
        print("ver el area de entrenamiento asignado")
    elif opc_menu_triner == "5":
        print("Gracias por usar nuestro programa")
    else:
        print("Ingrese uno de los números que aparecen en la lista")