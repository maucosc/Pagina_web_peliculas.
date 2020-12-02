from conexion import *
from textos import *


def eliminar_Usuario():
    print("----------------")
    print("Eliminar usuario")
    print("----------------")

    nickname = input("Introdusca el nombre exacto: ")
    passwd = input("Introdusca la contraseña como medida de seguridad: ")
    cursor = db.cursor()
    sql = "DELETE FROM cuenta WHERE nickname = '{}' AND passwd = SHA2('{}',0)".format(nickname, passwd)
    cursor.execute(sql)
    db.commit()
    text_dato_eliminado()


def eliminar_servidor_cuenta():
    print("--------------------------------------")
    print("Eliminar servidor y cuenta relacionada")
    print("--------------------------------------")

    nombre = input("Introduzca el nombre del servidor: ")
    cursor = db.cursor()
    sql = "DELETE servidor, cuenta  \
          FROM servidor  \
          INNER JOIN cuenta ON servidor.id_cuenta_fk = cuenta.id \
          WHERE servidor.nombre = '{}'".format(nombre)
    cursor.execute(sql)
    db.commit()
    text_dato_eliminado()
