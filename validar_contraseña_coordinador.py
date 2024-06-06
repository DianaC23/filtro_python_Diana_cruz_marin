from menu_del_coordinador import menu_coordinador_menu
#Cotraseña coordinador:coordi123
def validar_password():
    ingresar_password = input("por favor ingrese la contraseña: ")
    contra = "coordi123"
    if ingresar_password == contra:
        print("Bienvenido coordinador")
        menu_coordinador_menu()
    else:
        print("error por favor ingrese la contraseña correcta")
validar_password()