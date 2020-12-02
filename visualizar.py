from conexion import *


def visualizar_pelicula():

    while True:
        nombre = input("Ingrese nombre de pelicula: ")
        cursor = db.cursor()
        sql = "SELECT pelicula.id AS 'n°',"\
              "pelicula.nombre,"\
              "pelicula.resolucion,"\
              "pelicula.idioma m,"\
              "pelicula.tamano AS 'Tamaño',"\
              "categoria.nombre AS 'Categoria'"\
              "FROM "\
              "categoria_pelicula"\
              "INNER JOIN categoria ON categoria_pelicula.id_categoria_fk = categoria.id"\
              "INNER JOIN pelicula ON categoria_pelicula.id_pelicula_fk = pelicula.id"\
              "WHERE pelicula.nombre = '{}'".format(nombre).strip().lower()
        cursor.execute(sql)
        rs = cursor.fetchall()

        if rs != rs:
            print("")
            print("--------------------")
            print("Pelicula inexistente")
            print("--------------------")
        else:
            print(rs)


def visualizar_peliculas_disponibles():

    while True:
        cursor = db.cursor()
        sql = "SELECT pelicula.id AS 'n°',"\
              "pelicula.nombre,"\
              "pelicula.resolucion,"\
              "pelicula.idioma,"\
              "pelicula.tamano,"\
              "categoria.nombre AS 'Categoria',"\
              "FROM "\
              "categoria_pelicula"\
              "INNER JOIN categoria ON categoria_pelicula.id_categoria_fk = categoria.id"\
              "INNER JOIN pelicula ON categoria_pelicula.id_pelicula_fk = pelicula.id"
        cursor.execute(sql)
        rs = cursor.fetchall()

        for x in rs:
            print(x)
