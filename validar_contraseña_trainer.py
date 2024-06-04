import menu_del_trainer
def validar_password_trainer():
        ingresar_password = input("por favor ingrese la contraseña")
        password1 = "juanito123"
        password2 = "jholver123"
        password3 = "miguelito123"
        if ingresar_password == password1:
            print(f"Bienvenido trainer Juan")
            menu_del_trainer.menu_del_trainer_menu()
        else:
            print("error por favor ingrese la contraseña correcta")
            validar_password_trainer()
        if ingresar_password == password2:
            print(f"Bienvenido trainer Jholver")
            menu_del_trainer.menu_del_trainer_menu()
        else:
            print("error por favor ingrese la contraseña correcta")
            validar_password_trainer()
        if ingresar_password == password3:
            print("Bienvenido trainer Miguel")
            menu_del_trainer.menu_del_trainer_menu()
        else:
            print("error por favor ingrese la contraseña correcta")
            validar_password_trainer()
    #Cotraseña profesor 1 :juanito123
    #Cotraseña profesor 2 :jholver123
    #Cotraseña profesor 3 :miguelito123