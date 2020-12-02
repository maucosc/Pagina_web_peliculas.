from textos import *
from visualizar import *
from actualizar import *

def crear():
    while True:
        print("")
        print("Agregar Informacion")
        print("")
        print("A) ")
        print("B) ")
        print("C) ")
        print("D) Salir")

        op = input("Opcion: ")
        op = op.strip().lower()

        if op == "C":
            print("")
            print("----------")
            print("Regresando")
            print("----------")

        elif op == "A":
            pass

        elif op == "B":
            pass

        else:
            text_ingrese_op_valida()
            crear()


def visualizar():

    while True:

        text_menu_visualizar_text()
        op = input("Opcion: ")
        op = op.strip().lower()

        if op == "a" or op == "b" or op == "c":

            if op == "C":
                text_regresar()

            elif op == "A":
                visualizar_pelicula()

            elif op == "B":
                visualizar_peliculas_disponibles()
            break

        else:
            text_ingrese_op_valida()


def actualizar():

    while True:
        text_espacio()
        text_menu_actualizar()

        op = input("Opcion: ")
        op = op.strip().lower()

        if op == "C":
            text_regresar()

        elif op == "A":
            actualizar_usuario()

        elif op == "B":
            actualizar_pelicula()

        else:
            text_ingrese_op_valida()
            actualizar()


def eliminar():
    pass


def iniciar_sesion(nickname, passwd):

    while True:
        cursor = db.cursor()
        sql = "SELECT COUNT(*) FROM cuenta WHERE nickname = '{}' AND passwd = SHA2('{}',0)".format(nickname, passwd)
        cursor.execute(sql)
        rs = cursor.fetchall()

        if rs[0][0] != 0:
            while True:
                text_menu_iniciar_sesion()
                op = input("Opcion: ")
                op = op.strip().lower()

                if op == "e" or op == "salir":
                    text_mensaje_despedida()
                    menu_sesion()

                elif op == "A":
                    crear()

                elif op == "B":
                    visualizar()

                elif op == "C":
                    eliminar()

                else:
                    text_ingrese_op_valida()

        else:
            text_usuario_invalido()
            break


def crear_cuenta():
    cursor = db.cursor()
    nickname = input("Ingrese su nickname: ")
    email = input("Ingrese su correo: ")
    passwd = input("Ingrese su contraseña: ")
    sql = "INSERT INTO cuenta (nickname,email,passwd) VALUES ('{}','{}',SHA2('{}',0))".format(nickname, email, passwd)
    cursor.execute(sql)
    db.commit()
    text_usuario_creado()


def menu_sesion():
    text_mensaje_bienvenida()

    while True:
        print("")
        print("A) Iniciar Sesion")
        print("B) Crear Cuenta")
        print("C) Salir")
        op = input("Ingrese opcion: ")
        op = op.strip().lower()

        if op == 'c':
            text_mensaje_despedida()
            break

        elif op == 'a':
            nickname = input("Ingrese su nickname: ")
            passwd = input("Ingrese su contraseña: ")
            iniciar_sesion(nickname, passwd)

        elif op == 'b':
            crear_cuenta()

        elif op == 'c':
            text_ingrese_op_valida()


menu_sesion()
