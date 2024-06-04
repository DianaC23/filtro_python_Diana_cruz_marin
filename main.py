while True:
    print("Bienvenido a campus app")
    print("Seguimiento academico de los Campers")
    print("Por favor indique su rol")
    roles = (
         "1. Coordinador\n"
         "2. Trainer\n"
         "3. Camper\n"
         "4. inscribirse como camper\n"
         "5. Para salir\n"
    )
    print(roles)
    opc_roles = input("- ") 
    if opc_roles == "6":
       print("error")
    elif opc_roles == "2" or opc_roles == "trainer" or opc_roles == "Trainer":
        import validar_contraseña_trainer
        validar_contraseña_trainer.validar_password_trainer()
    elif opc_roles == "3" or opc_roles.lower()== "camper":
        print("camper")
        print("Bienvenido camper")
        print("¿Que te gustaria hacer?")
        opc_menu_camper = (
            "Presiona 1 si quieres confirmar que estas inscrito \n"
            "presione 2 si quiere leer tus datos \n"
            "presione 3 si quieres actualizar tus datos \n"
            "presione 4 si quiere eliminar su usuario \n"
            "presione 5 para ver su ruta \n"
            "presione 6 salir")
        print(opc_menu_camper)
        opc_menu_cmper = input("- ")
        if opc_menu_cmper == "1":
            print("confirmar que estas inscrito")

        elif opc_menu_camper == 2:
            print("leer tus datos")
        elif opc_menu_camper == 3:
            print("Actualizar")
        elif opc_menu_camper == 4:
            print("eliminar su usuario")
        elif opc_menu_camper == 5:
            print("ver su ruta")
        elif opc_menu_camper == 6:
            print("Gracias por usar nuestro programa")
            break
        else:
             print("error por favor ingrese uno de los valores que aparecen en pantalla")
    elif opc_roles == "inscribirse como camper" or opc_roles == "Inscribirse como camper" or opc_roles == "4":
        import agregar_campers
        agregar_campers.ingresar_datos_d_camper()
    elif opc_roles == "salir" or opc_roles == "Salir" or opc_roles == "5":
        print("Gracias por usar nuestro programa")
        break
    elif opc_roles =="1" or opc_roles == "coordinador" or opc_roles == "Coordinador" or opc_roles == "COORDINADOR":
        import validar_contraseña_coordinador
        validar_contraseña_coordinador.validar_password()
    else:
        print("error por favor ingrese uno de los tres valores")