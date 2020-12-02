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

        elif op == "a":
            email = input("Ingrese el email que desea modificar: ")
            email_new = input("Ingrese el nuevo email: ")

            sql = "UPDATE cuenta SET email = '{}' WHERE email = '{}'".format(email_new, email)
            cursor.execute(sql)
            text_modificacion_exitosa()

        elif op == "b":

            usuario = input("Ingrese el nombre del usuario que desea modificar: ")
            usuario_new = input("Ingrese el nuevo nombre de usuario: ")

            sql = "UPDATE cuenta SET nickname = '{}' WHERE nickname = '{}'".format(usuario_new, usuario)
            cursor.execute(sql)
            text_modificacion_exitosa()

        else:

            text_ingrese_op_valida()
            actualizar_usuario()


def actualizar_pelicula():

    while True:
        cursor = db.cursor()

        print("Actualizar datos de pelicula")
        print("")
        print("A) nombre de pelicula")
        print("B) idioma de pelicula")
        print("C) Regresar")

        op = input("Opcion: ")
        op = op.strip().lower()

        if op == "C":
            print("")
            print("----------")
            print("Regresando")
            print("----------")
            print("")

        elif op == "A":
            pelicula = input("Ingrese el nombre que desea cambiar: ")
            pelicula_new = input("Ingrese el nuevo nombre de la pelicula ")

            cursor.execute("UPDATE pelicula SET nombre = '{}' WHERE nombre = '{}';".format(pelicula_new, pelicula).strip().lower())
        elif op == "B":
            pelicula = input("Ingrese el idioma de la pelicula que deseamodificar ")
            pelicula_new = input("Ingrese el nuevo idioma de la pelicula: ")

            cursor.execute("UPDATE pelicula SET nombre = '{}' WHERE nombre = '{}';".format(pelicula_new, pelicula).strip().lower())
        else:
            print("Ingrese una opcion valida")
            actualizar_pelicula()


