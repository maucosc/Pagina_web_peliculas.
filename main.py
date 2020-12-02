from conexion import *


def crear():
    pass


def visualizar():
    pass


def actualizar():
    pass


def eliminar():
    pass


def iniciarSesion():
    while (True):
        nickname = input("Ingrese su nombre de usuario: ")
        passwd = input("Ingrese su contraseña: ")
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM cuenta WHERE nickname = '{}' AND passwd = SHA2('{}',0)".format(nickname,
                                                                                                            passwd).lower().strip())
        rs = cursor.fetchall()
        if (rs[0][0] == 0):
            while (True):
                print("----")
                print("Menu")
                print("")
                print("A) Crear")
                print("B) Visualizar Datos")
                print("C) Actualizar Datos")
                print("D) Eliminar Datos")
                print("E) Regresar a menu")

                op1 = input("Opcion: ")
                op1 = op1.strip().lower()

                if (op1 == 'e' or op1 == 'salir'):
                    print("-------------")
                    print("Vuelva pronto")
                    print("-------------")
                    print()
                    menuSesion()
                elif (op1 == 'a'):
                    visualizar()
                elif (op1 == 'b'):
                    visualizar()
                elif (op1 == 'c'):
                    actualizar()
                elif (op1 == 'd'):
                    eliminar()
                elif (op1 != 'a' or op1 != 'b' or op1 != 'c' or op1 != 'd' or op1 != 'e'):
                    print("                         ")
                    print("Ingrese una opcion valida")
                    print("                         ")
                    iniciarSesion()
        else:
            print("---------------")
            print("Opcion invalida")
            print("---------------")
            break


def menuSesion():
    print("")
    while (True):
        print("")
        print("Bienvenido")
        print("")
        print("1) Iniciar Sesion")
        print("2) Crear Cuenta")
        print("3) Salir")
        op1 = input("opcion: ")
        op1 = op1.strip().lower()

        if op1 == "3":
            print("-------------------")
            print("Adios vuelva pronto")
            print("-------------------")
            exit()
        elif op1 == "1":
            iniciarSesion()
        elif op1 == "2":
            crearCuenta()
        else:
            print("               ")
            print("---------------")
            print("Opcion invalida")
            print("---------------")
        espacios()


menuSesion()
