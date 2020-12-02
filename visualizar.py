from conexion import *
from textos import text_espacio


def visualizar_pelicula():

    while True:
        nombre = input("Ingrese nombre de pelicula: ")
        cursor = db.cursor()
        sql = "SELECT pelicula.nombre,\
                pelicula.resolucion,\
                pelicula.idioma,\
                pelicula.tamano,\
                categoria.nombre AS 'Categoria', \
                pelicula.sinopsis\
                FROM categoria_pelicula\
                LEFT JOIN categoria ON categoria_pelicula.id_categoria_fk = categoria.id\
                RIGHT JOIN pelicula ON categoria_pelicula.id_pelicula_fk = pelicula.id\
                WHERE pelicula.nombre LIKE '%{}%'".format(nombre).strip().lower()
        cursor.execute(sql)
        rs = cursor.fetchall()

        if rs != rs:
            print("")
            print("--------------------")
            print("Pelicula inexistente")
            print("--------------------")
        else:
            for x in rs:
                print(x)
        break


def visualizar_peliculas_disponibles():

    cursor = db.cursor()
    sql = "SELECT pelicula.nombre,\
            pelicula.resolucion,\
            pelicula.idioma,\
            pelicula.tamano,\
            categoria.nombre AS 'Categoria', \
            pelicula.sinopsis\
            FROM categoria_pelicula\
            LEFT JOIN categoria ON categoria_pelicula.id_categoria_fk = categoria.id\
            RIGHT JOIN pelicula ON categoria_pelicula.id_pelicula_fk = pelicula.id"
    cursor.execute(sql)
    rs = cursor.fetchall()

    text_espacio()
    for x in rs:
        print(x)

def visualizar_usuario():
    text_espacio()
    cursor = db.cursor()
    sql = "SELECT cuenta.nickname, cuenta.email FROM cuenta"
    cursor.execute(sql)
    rs = cursor.fetchall()
    db.commit()
    for x in rs:
        print(x)
