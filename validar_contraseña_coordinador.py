import menu_del_coordinador
#Cotraseña coordinador:coordi123
def validar_password():
    ingresar_password = input("por favor ingrese la contraseña")
    contra = "coordi123"
    if ingresar_password == contra:
        print("Bienvenido coordinador")
        menu_del_coordinador.menu_coordinador_menu()
    else:
        print("error por favor ingrese la contraseña correcta")
validar_password()