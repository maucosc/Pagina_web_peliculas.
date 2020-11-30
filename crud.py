from main import IniciarSesion
from conexion import *


def crearCuanta():

    cursor = db.cursor()
    nickname = input("Ingrese el nombre de usuario: ")
    email = input("Ingrese su Correo: ")
    passwd = input("Ingrese su contraseña: ")
    cursor.execute("INSERT INTO cuenta (nickname,email,passwd) VALUES ('{}','{}',SHA2('{}',0));".format(nickname,email,passwd))
    db.commit()


def insertarPelicula():
    pass

def visualizar():
    while (True):
        nombre = input("Buscar pelicula")
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
            print("Pelicula invalida")
            print("")
            print("")
        else:
            print(rs)

        for x in rs:
            print(x)

def actualizar():
    pass

def borrar():
    while(True):
        print("Eliminar datos")
        print("")
        print("A) Usuario")
        print("B) Pelicula")

        op = input("opcion:")
        op = op.strip().lower()

        if(op == "a"):
            nombre = input("introduzca el nombre del usuario que desea eliminar: ")
            passwd = input("Ingrese la contraseña como medidad de seguridad: ")
            cursor = db.cursor()
            rs = cursor.fetchall()
            if(rs[0][0] == 0):
                print("                              ")
                print("Usuario o contraseña invalidos")
                print("                              ")
            else:
                cursor.execute("DELETE FORM cuenta WHERE nickname = '{}';".format(nombre,passwd))
                print("")
                print("Eliminacion exitosa")
                IniciarSesion()
        elif(op == "b"):
            nombre = input("Introdusca el nombre de la pelicula: ")
            fecha = input("ingrese fecha de pelicula: ")
            cursor = db.cursor()
            cursor.execute("SELECT COUNT(*) pelicula WHERE nombre = '{}' AND fecha '{}';".format(nombre,fecha))
            rs = cursor.fetchall()
            if (rs[0][0] == 0):
                print("                              ")
                print("Usuario o contraseña invalidos")
                print("                              ")
            else:
                cursor.execute("DELETE FORM pelicula WHERE nombre = '{}';".format(nombre, fecha))