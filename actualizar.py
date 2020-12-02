from conexion import *
from textos import *


def actualizar_usuario():
    while True:
        cursor = db.cursor()
        text_menu_actualizar_usuario()

        op = input("Opcion: ")
        op = op.strip().lower()

        if op == "c":
            text_regresar()
            break
        elif op == "a":
            print("")
            email = input("Ingrese el email que desea modificar: ")
            email_new = input("Ingrese el nuevo email: ")

            sql = "UPDATE cuenta SET email = '{}' WHERE email = '{}'".format(email_new, email)
            cursor.execute(sql)
            db.commit()
            text_espacio()
            text_modificacion_exitosa()

        elif op == "b":
            print("")
            usuario = input("Ingrese el nombre del usuario que desea modificar: ")
            usuario_new = input("Ingrese el nuevo nombre de usuario: ")

            sql = "UPDATE cuenta SET nickname = '{}' WHERE nickname = '{}'".format(usuario_new, usuario)
            cursor.execute(sql)
            db.commit()
            text_espacio()
            text_modificacion_exitosa()

        else:
            text_ingrese_op_valida()
            break

def actualizar_pelicula():

    while True:
        cursor = db.cursor()
        text_menu_actualizar_pelicula()

        op = input("Opcion: ")
        op = op.strip().lower()

        if op == "c":
            text_regresar()
            break

        elif op == "a":
            text_espacio()
            pelicula = input("Ingrese el nombre que desea cambiar: ")
            pelicula_new = input("Ingrese el nuevo nombre de la pelicula: ")

            sql = "UPDATE pelicula SET nombre = '{}' WHERE nombre = '{}';".format(pelicula_new, pelicula)
            cursor.execute(sql)
            db.commit()
            text_espacio()
            text_modificacion_exitosa()

        elif op == "b":
            text_espacio()
            pelicula = input("Ingrese el nombre de la pelicula: ")
            pelicula_new = input("Ingrese el nuevo idioma de la pelicula: ")

            sql = "UPDATE pelicula SET idioma = '{}' WHERE nombre = '{}';".format(pelicula_new, pelicula)
            cursor.execute(sql)
            db.commit()
            text_espacio()
            text_modificacion_exitosa()
        else:
            print("Ingrese una opcion valida")
            actualizar_pelicula()


