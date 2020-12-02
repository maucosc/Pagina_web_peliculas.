from conexion import *
from textos import *


def ingresar_pelicula():
    while True:
        print("-----------------------")
        print("Informacion de pelicula")
        print("-----------------------")
        cursor = db.cursor()
        nombre = input("Ingrese nombre de pelicula: ")
        resolucion = input("Ingrese la resolucion de la pelicula: ")
        idioma = input("Ingrese el idioma de la pelicula: ")
        tamano = input("Ingrese el tamaño en GB de la pelicula: ")
        sinopsis = input("Ingrese una breve descripcion de la pelicula: ")

        sql = "INSERT INTO pelicula (nombre,resolucion,idioma,tamano,sinopsis) VALUES ('{}','{}','{}','{}','{}')" \
            .format(nombre, resolucion, idioma, tamano, sinopsis)
        cursor.execute(sql)
        db.commit()
        text_pelicula_creada()
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