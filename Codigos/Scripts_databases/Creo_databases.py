import sqlite3

class ErrorCrearTabla(Exception):
    def __str__(self):
        return "No se pudo crear la tabla, verifique las direcciones de las carpetas"

def Creo_databases():
    #Primero creo la base de datos.
    database = sqlite3.connect('..\\..\\Databases\\Academia.db')

    cursor = database.cursor()

    print (u"la base de datos se creo correctamente")

    #Primero creo la tabla de usuarios.
    try:
        cursor.execute("create table Usuarios\
          (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
          username TEXT NOT NULL UNIQUE,\
          password TEXT NOT NULL,\
          privilegios INTEGER NOT NULL)")

        print("La tabla Usuarios fue creada correctamente")
    except sqlite3.OperationalError as e:
        if str(e) == "table Usuarios already exists":
            print("La tabla Usuarios ya estaba creada")
        else:
            raise ErrorCrearTabla

    #ahora que la base esta creada, creo el usuario root
    try:
        cursor.execute("INSERT INTO Usuarios\
          (username,password,privilegios)\
          VALUES('root','4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2',1)")
        print("El usuairo root se inserto correctamente")
        database.commit()
    except Exception as e:
        print("Error al crear el usuario root, en el modulo creo_databases -> " + str(e))

        #Comiteo los cambios a la base de datos.
        database.commit()

    #Creo las tablas. Primero la tabla de los alumnos
    try:
        cursor.execute("create table Alumnos\
          (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
          Nombre TEXT not null,\
          Apellido TEXT not null,\
          Fecha_nacimiento char(50),\
          DNI int not null,\
          Email char(50),\
          Telefono char(50))")

        print("La tabla Alumnos fue creada correctamente")
    except sqlite3.OperationalError as e:
        if str(e) == "table Alumnos already exists":
            print("La tabla Alumnos ya estaba creada")
        else:
            raise ErrorCrearTabla

    #Ahora creo la tabla de los docentes.
    try:
        cursor.execute("create table Docentes\
          (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
           Nombre TEXT not null,\
          Apellido TEXT not null,\
          Fecha_nacimiento char(50),\
          DNI int not null,\
          Email char(50),\
          Telefono char(50))")

        print("La tabla Docentes fue creada correctamente")
    except sqlite3.OperationalError as e:
        if str(e) == "table Docentes already exists":
            print("La tabla Docentes ya estaba creada")
        else:
            raise ErrorCrearTabla

    # Ahora creo la tabla de los Niveles.
    try:
        cursor.execute("create table Nivel\
          (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
          Nivel TEXT not null,\
          Porcentaje_docente int)")

        print("La tabla Nivel fue creada correctamente")
    except sqlite3.OperationalError as e:
        if str(e) == "table Nivel already exists":
            print("La tabla Nivel ya estaba creada")
        else:
            raise ErrorCrearTabla

    # Ahora creo la tabla de las materias.
    try:
        cursor.execute("create table Materias\
          (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
          Materia TEXT not null,\
          ID_nivel int REFERENCES Nivel(ID))")

        print("La tabla Materias fue creada correctamente")
    except sqlite3.OperationalError as e:
        if str(e) == "table Materias already exists":
            print("La tabla Materias ya estaba creada")
        else:
            raise ErrorCrearTabla

    # Ahora creo la tabla de las Aulas.
    try:
        cursor.execute("create table Aulas\
          (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
          Nombre TEXT not null,\
           CLub_de_la_Tarea boolean not null)")

        print("La tabla Aulas fue creada correctamente")
    except sqlite3.OperationalError as e:
        if str(e) == "table Aulas already exists":
            print("La tabla Aulas ya estaba creada")
        else:
            raise ErrorCrearTabla

    # Ahora creo la tabla de las Docentes-Materias.
    try:
        cursor.execute("create table Docentes_y_Materias\
          (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
          ID_mat int references Materias(ID),\
          ID_doc int references Docentes(ID))")

        print("La tabla Docentes_y_Materias fue creada correctamente")
    except sqlite3.OperationalError as e:
        if str(e) == "table Docentes_y_Materias already exists":
            print("La tabla Docentes_y_Materias ya estaba creada")
        else:
            raise ErrorCrearTabla

    # Ahora creo la tabla de las Cantidad de clases en el paquete.
    try:
        cursor.execute("create table Cant_clas_por_paquete\
          (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
          cantidad int)")

        print("La tabla Cant_clas_por_paquete fue creada correctamente")
    except sqlite3.OperationalError as e:
        if str(e) == "table Cant_clas_por_paquete already exists":
            print("La tabla Cant_clas_por_paquete ya estaba creada")
        else:
            raise ErrorCrearTabla

    # Ahora creo la tabla de los costos de las clases.
    try:
        cursor.execute("create table Costo_clase\
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        ID_cant_clas int references Cant_clas_por_paquete(ID),\
        particular boolean not null,\
        costo_total int,\
        costo_unitario int)")

        print("La tabla Costo_clase fue creada correctamente")
    except sqlite3.OperationalError as e:
        if str(e) == "table Costo_clase already exists":
            print("La tabla Costo_clase ya estaba creada")
        else:
            raise ErrorCrearTabla

    # Ahora creo la tabla de las clases.
    try:
        cursor.execute("create table clases\
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        ID_docente int references docentes(ID),\
        ID_materia int references materias(ID),\
        ID_aula int references aulas(ID),\
        ID_costo_clases int REFERENCES costo_clase(ID),\
        reprogramo boolean,\
        horario char(50))")

        print("La tabla clases fue creada correctamente")
    except sqlite3.OperationalError as e:
        if str(e) == "table clases already exists":
            print("La tabla clases ya estaba creada")
        else:
            raise ErrorCrearTabla

    # Ahora creo la tabla de las alumnos_y_clases.
    try:
        cursor.execute("create table alumnos_y_clases\
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        ID_alumno int references alumnos(ID),\
        ID_clase int references clases(ID),\
        asistio boolean)")

        print("La tabla alumnos_y_clases fue creada correctamente")
    except sqlite3.OperationalError as e:
        if str(e) == "table alumnos_y_clases already exists":
            print("La tabla alumnos_y_clases ya estaba creada")
        else:
            raise ErrorCrearTabla

if __name__ == "__main__":
    Creo_databases()