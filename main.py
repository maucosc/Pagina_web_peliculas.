from eliminar import *
from insertar import *
from textos import *
from visualizar import *
from actualizar import *


def crear():
    while True:
        text_menu_agregar()

        op = input("Opcion: ")
        op = op.strip().lower()

        if op == "c":
            text_regresar()
            break

        elif op == "a":
            ingresar_pelicula()

        elif op == "b":
            crear_cuenta()
        else:
            text_ingrese_op_valida()
            crear()


def visualizar():

    while True:

        text_menu_visualizar_text()
        op = input("Opcion: ")
        op = op.strip().lower()

        if op == "a" or op == "b" or op == "c" or op == "d":

            if op == "d":
                text_regresar()
                break
            elif op == "a":
                visualizar_usuario()
            elif op == "b":
                visualizar_pelicula()

            elif op == "c":
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

        if op == "c":
            text_regresar()
            break

        elif op == "a":
            actualizar_usuario()

        elif op == "b":
            actualizar_pelicula()

        else:
            text_ingrese_op_valida()
            actualizar()


def eliminar():
    while True:
        text_menu_eliminar()

        op = input("Opcion: ")
        op = op.strip().lower()

        if op == "c":
            text_regresar()
            break

        elif op == "a":
            eliminar_Usuario()

        elif op == "b":
            eliminar_servidor_cuenta()

        else:
            text_ingrese_op_valida()
            eliminar()


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

                elif op == "a":
                    crear()

                elif op == "b":
                    visualizar()

                elif op == "c":
                    actualizar()

                elif op == "d":
                    eliminar()
                else:
                    text_ingrese_op_valida()

        else:
            text_usuario_invalido()
            break

def menu_sesion():
    text_mensaje_bienvenida()

    while True:
        print("")
        print("A) Iniciar Sesion")
        print("B) Salir")
        op = input("Ingrese opcion: ")
        op = op.strip().lower()

        if op == 'b':
            text_mensaje_despedida()
            exit()

        elif op == 'a':
            print("")
            nickname = input("Ingrese su nickname: ")
            passwd = input("Ingrese su contraseña: ")
            iniciar_sesion(nickname, passwd)

        else:
            text_ingrese_op_valida()
            menu_sesion()



menu_sesion()
