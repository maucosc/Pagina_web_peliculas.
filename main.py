import mysql.connector
db = mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="",
                             database="Arriendo_peliculas")

def actualizar():
    pass

def espacios():

    l = 0
    while (l <= 5):
        l += 1
        print("")

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
                cursor.execute("DELETE FORM cuenta WHERE nickname = '{}';".format(nombre))
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

def IniciarSesion():
    while(True):
        nickname = input("Ingrese su nombre de usuario: ")
        passwd = input("Ingrese su contraseña: ")
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM cuenta WHERE nickname = '{}' AND passwd = SHA2('{}',0)".format(nickname,passwd).lower().strip())
        rs = cursor.fetchall()

        if (rs[0][0] == 0):
            espacios()
            print("                                ")
            print("Usuario o contraseña incorrectas")
            print("                                ")

        else:
            espacios()
            while(True):
                print("         ")
                print("Saludos  ")
                print("         ")

                print("a) Actualizar")
                print("b) Borrar")
                print("c) Visualizar")
                print("d) Salir")
                op = input("Opcion: ")
                op = op.strip().lower()

                if (op == 'd' or op == 'salir'):
                    print("             ")
                    print("Vuelva Pronto")
                    print("             ")
                    break
                elif (op == "A"):
                    actualizar()
                elif (op == "B"):
                    borrar()
                elif (op == "C"):
                    visualizar()
                elif (op != "a" or op != "b" or op != "c"):
                    espacios()

            espacios()
            break
def CrearCuenta():

    cursor = db.cursor()
    nickname = input("Ingrese el nombre de usuario: ")
    email = input("Ingrese su Correo: ")
    passwd = input("Ingrese su contraseña: ")
    cursor.execute("INSERT INTO cuenta (nickname,email,passwd) VALUES ('{}','{}',SHA2('{}',0));".format(nickname, email, passwd))
    print("                           ")
    print("Usuario creado exitosamente")
    print("                           ")
    espacios()
    db.commit()

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
            break

def MenuSesion():
    print("")
    while(True):
        print("A) Iniciar sesion")
        print("B) Crear Usuario")
        print("C) Salir")
        op1 = input("Opcion: ")
        op1 = op1.strip().lower()
        if(op1 == "c"):
            espacios()
            print("Adios Vuelva pronto")
            print("                   ")
            break
        elif(op1 == "a"):
            IniciarSesion()

        elif (op1 == "b"):
            CrearCuenta()

        elif (op1 != "a" or op1 != "b" or op1 != "c"):
            espacios()

MenuSesion()