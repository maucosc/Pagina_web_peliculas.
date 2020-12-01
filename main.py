from crud import *
from conexion import *


def espacios():
    espacio = 0
    while (espacio <= 5):
        espacio += 1
        print("")


def crearCuenta():
    print("")
    cursor = db.cursor()
    nickname = input("Ingrese el nombre de usuario: ")
    email = input("ingrese un correo: ")
    passwd = input("Ingrese su contraseña: ")
    cursor.execute(
        "INSERT INTO cuenta (nickname,email,passwd) VALUES ('{}','{}',SHA2('{}',0));".format(nickname, email, passwd))
    db.commit()


def crear():
    pass


def ingresarPelicula():
    pass


def ingresarFormato():
    pass


def ingresarServidor():
    pass


def insertar():
    print("")
    while (True):
        print("----------")
        print("Bienvenido")
        print("----------")
        print("")
        print("A) Ingresar pelicula")
        print("B) Ingresar Servidor")
        print("C) Ingresar formato a pelicula")
        print("D) Salir")
        print("")

        op1 = input("Ingrese su respuesta:")
        op1 = op1.strip().lower()

        if (op1 == "c" or op1 == "salir"):
            espacios()
            print("-------------------")
            print("Adios vuelva pronto")
            print("-------------------")
            menuSesion()
        elif (op1 == "a"):
            ingresarPelicula()
        elif (op1 == "b"):
            ingresarServidor()
        elif (op1 == "a"):
            ingresarFormato()
        elif (op1 != "a" or op1 != "b" or op1 != "c" or op1 != "d"):
            print("---------------")
            print("Opcion invalida")
            print("---------------")
            insertar()

def visualizarPelicula():
    while (True):
        nombre = input("Buscar Pelicula")
        cursor = db.cursor()
        cursor.execute("SELECT pelicula.id AS 'N°',"
                       "pelicula.nombre,"
                       "pelicula.fecha,"
                       "pelicula.resolucion,"
                       "pelicula.idioma,"
                       "pelicula.tamano AS 'Tamaño',"
                       "categoria.nombre AS 'Categoria'"
                       "pelicula.sinopsis"
                       "FROM"
                       "categoria"
                       "INNERT JOIN categoria_pelicula ON categoria_pelicula.id_categoria_fk = categoria.id"
                       "INNERT JOIN pelicula ON categoria_pelicula.id_pelicula_fk = pelicula.id"
                       "WHERE pelicula.nombre LIKE '%{}%';".format(nombre))
        rs = cursor.fetchall()
        if(rs != rs):
            print("")
            print("Pelicula invalida")
            print("")
        else:
            for x in rs:
                print(x)


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
                print("----")
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
