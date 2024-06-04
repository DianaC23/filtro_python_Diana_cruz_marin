import asignar_notas_de_trainer
def menu_del_trainer_menu():
    opc_menu_trainer = (
    "1 Para poner notas a estudiantes\n"
    "2 Para salir"
        )
    print(opc_menu_trainer)
    opc_menu_triner = input("- ")
    
    if opc_menu_triner == "1":
        print("poner notas a estudiantes")
        asignar_notas_de_trainer.asignar_las_notas_del_camper()
    else:
        print("Ingrese uno de los números que aparecen en la lista")