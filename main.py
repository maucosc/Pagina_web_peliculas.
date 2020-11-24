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
    pass

def IniciarSesion():
    while(True):
        nickname = input("Ingrese su nombre de usuario: ")
        passwrd = input("Ingrese su contraseña: ")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM cuenta WHERE nickname = '{}' AND passwd = SHA2('{}',0)".format(nickname,passwrd).lower().strip())
        rs = cursor.fetchall()

        if (rs[0][0] == 0):
            print("")
            print("")
            print("")

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

                if (op == 'd'
                        or op == 'salir'
                ):
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
        print("B) Crear Usuario")
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
            espacios()

Menu()
