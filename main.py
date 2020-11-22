import mysql.connector
db = mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="",
                             database="descarga_peliculas")

def actualizar():
    pass

def espacios():

    l = 0
    while (l <= 5):
        l += 1
        print("")

def borrar():
    pass

def IniciarSesion():
    pass

def CrearCuenta():
    nickname = input("\033[1;30m Ingrese el nombre de usuario: ")
    email = input("Ingrese su Correo: ")
    passwrd = input("Ingrese su contraseña: ")
    cursor = db.cursor()
    cursor.execute("INSERT INTO cuenta VALUES('NULL','{}','{}',SHA2('{}',0);".format(nickname, email, passwrd))


def visualizar():
    pass

def Menu():
    print("")
    while(True):
        print("A) Iniciar sesion")
        print("B) Crear sesion")
        print("C) Salir")
        op1 = input("Opcion: ")
        op1 = op1.strip().lower()
        if(op1 == "c"):
            espacios()
            print("adios")
            break
        elif(op1 == "a"):
            IniciarSesion()

        elif (op1 == "b"):
            CrearCuenta()

        elif (op1 != "a" or op1 != "b" or op1 != "c"):
            l = 0
            while (l <= 5):
                l += 1
                print("")

Menu()
