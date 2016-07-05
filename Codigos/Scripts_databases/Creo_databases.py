import mysql.connector

class ErrorCrearTabla(Exception):
    def __str__(self):
        return "No se pudo crear la tabla, verifique las direcciones de las carpetas"

def Creo_databases():
    #Primero creo la base de datos.
    database = mysql.connector.connect(user='root',password='root',host='127.0.0.1')
    cursor = database.cursor()
    print("Conexion exitosa al servidor de base de datos")

    try:
        cursor.execute("CREATE DATABASE academia")
    except Exception as e:
        if str(e.args[0]) == str(1007):
            print("La base de datos academia ya estaba creada")
        else:
            print(e)

    cursor.execute("use academia")
    print("conexion a la base de datos academia exitosa")
    #Primero creo la tabla de usuarios.
    try:
        cursor.execute("create table Usuarios\
          (ID INTEGER PRIMARY KEY AUTO_INCREMENT,\
          username VARCHAR(100) NOT NULL UNIQUE,\
          password VARCHAR(100) NOT NULL,\
          privilegios INTEGER NOT NULL)")

        print("La tabla Usuarios fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla Usuarios ya estaba creada")
        else:
            print(e)

    #ahora que la base esta creada, creo el usuario root
    try:
        cursor.execute("INSERT INTO Usuarios\
          (username,password,privilegios)\
          VALUES('root','4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2',1)")
        print("El usuairo root se inserto correctamente")
        database.commit()
    except Exception as e:
        if str(e.args[0]) == str(1062):
            print("El usuario root ya esta creado")
        else:
            print(e)



    #Creo las tablas. Primero la tabla de los alumnos
    try:
        cursor.execute("create table Alumnos\
          (ID INTEGER PRIMARY KEY AUTO_INCREMENT,\
          Nombre VARCHAR(100) not null,\
          Apellido VARCHAR(100) not null,\
          Fecha_nacimiento VARCHAR(100),\
          DNI int not null,\
          Email VARCHAR(100),\
          Telefono VARCHAR(100))")

        print("La tabla Alumnos fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla alumnos ya estaba creada")
        else:
            print(e)

    #Ahora creo la tabla de los docentes.
    try:
        cursor.execute("create table Docentes\
          (ID INTEGER PRIMARY KEY AUTO_INCREMENT,\
           Nombre VARCHAR(100) not null,\
          Apellido VARCHAR(100) not null,\
          Fecha_nacimiento VARCHAR(100),\
          DNI int not null,\
          Email VARCHAR(100),\
          Telefono VARCHAR(100))")

        print("La tabla Docentes fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla docentes ya estaba creada")
        else:
            print(e)

    # Ahora creo la tabla de los Niveles.
    try:
        cursor.execute("create table Nivel\
          (ID INTEGER PRIMARY KEY AUTO_INCREMENT,\
          Nivel VARCHAR(100) not null,\
          Porcentaje_docente int)")

        print("La tabla Nivel fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla Niveles ya estaba creada")
        else:
            print(e)

    # Ahora creo la tabla de las materias.
    try:
        cursor.execute("create table Materias\
          (ID INTEGER PRIMARY KEY AUTO_INCREMENT,\
          Materia VARCHAR(100) not null,\
          ID_nivel int REFERENCES Nivel(ID))")

        print("La tabla Materias fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla materias ya estaba creada")
        else:
            print(e)

    # Ahora creo la tabla de las Aulas.
    try:
        cursor.execute("create table Aulas\
          (ID INTEGER PRIMARY KEY AUTO_INCREMENT,\
          Nombre VARCHAR(100) not null,\
           CLub_de_la_Tarea boolean not null)")

        print("La tabla Aulas fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla Aulas ya estaba creada")
        else:
            print(e)

    # Ahora creo la tabla de las Docentes-Materias.
    try:
        cursor.execute("create table Docentes_y_Materias\
          (ID INTEGER PRIMARY KEY AUTO_INCREMENT,\
          ID_mat int references Materias(ID),\
          ID_doc int references Docentes(ID))")

        print("La tabla Docentes_y_Materias fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla Docentes-Materias ya estaba creada")
        else:
            print(e)

    # Ahora creo la tabla de las Cantidad de clases en el paquete.
    try:
        cursor.execute("create table Cant_clas_por_paquete\
          (ID INTEGER PRIMARY KEY AUTO_INCREMENT,\
          cantidad int)")

        print("La tabla Cant_clas_por_paquete fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla Cantidad de clases en el paquete ya estaba creada")
        else:
            print(e)

    # Ahora creo la tabla de los costos de las clases.
    try:
        cursor.execute("create table Costo_clase\
        (ID INTEGER PRIMARY KEY AUTO_INCREMENT,\
        ID_cant_clas int references Cant_clas_por_paquete(ID),\
        particular boolean not null,\
        costo_total int,\
        costo_unitario int)")

        print("La tabla Costo_clase fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla costos de las clases ya estaba creada")
        else:
            print(e)

    # Ahora creo la tabla de las clases.
    try:
        cursor.execute("create table clases\
        (ID INTEGER PRIMARY KEY AUTO_INCREMENT,\
        ID_docente int references docentes(ID),\
        ID_materia int references materias(ID),\
        ID_aula int references aulas(ID),\
        ID_costo_clases int REFERENCES costo_clase(ID),\
        reprogramo boolean,\
        horario VARCHAR(100))")

        print("La tabla clases fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla clases ya estaba creada")
        else:
            print(e)

    # Ahora creo la tabla de las alumnos_y_clases.
    try:
        cursor.execute("create table alumnos_y_clases\
        (ID INTEGER PRIMARY KEY AUTO_INCREMENT,\
        ID_alumno int references alumnos(ID),\
        ID_clase int references clases(ID),\
        asistio boolean)")

        print("La tabla alumnos_y_clases fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla alumnos_y_clases ya estaba creada")
        else:
            print(e)

if __name__ == "__main__":
    Creo_databases()