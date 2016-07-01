import sqlite3


#Primero creo la base de datos.
database = sqlite3.connect('..\\..\\Databases\\Academia.db')

cursor = database.cursor()

print (u"la base de datos se creo correctamente")

#Primero creo la tabla de usuarios.
try:
    cursor.execute("create table Usuarios\
      (ID_usuarios INTEGER PRIMARY KEY AUTOINCREMENT,\
      username TEXT NOT NULL UNIQUE,\
      password TEXT NOT NULL,\
      privilegios INTEGER NOT NULL)")

    print("La tabla Usuarios fue creada correctamente")
except sqlite3.OperationalError as e:
    if str(e) == "table Usuarios already exists":
        print("La tabla Usuarios ya estaba creada")
    else:
        print("No se pudo crear la tabla Usuarios")
        print(e)
        exit()

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
      (ID_alumnos INTEGER PRIMARY KEY AUTOINCREMENT,\
      Nombre_y_Apellido TEXT not null,\
      Fecha_nacimiento char(50),\
      DNI int not null,\
      Email char(50),\
      Telefono char(50))")

    print("La tabla Alumnos fue creada correctamente")
except sqlite3.OperationalError as e:
    if str(e) == "table Alumnos already exists":
        print("La tabla Alumnos ya estaba creada")
    else:
        print("No se pudo crear la tabla Alumnos")
        exit()

#Ahora creo la tabla de los docentes.
try:
    cursor.execute("create table Docentes\
      (ID_docentes INTEGER PRIMARY KEY AUTOINCREMENT,\
      Nombre_y_Apellido TEXT not null,\
      Fecha_nacimiento char(50),\
      DNI int not null,\
      Email char(50),\
      Telefono char(50))")

    print("La tabla Docentes fue creada correctamente")
except sqlite3.OperationalError as e:
    if str(e) == "table Docentes already exists":
        print("La tabla Docentes ya estaba creada")
    else:
        print("No se pudo crear la tabla Docentes")
        exit()

# Ahora creo la tabla de los Niveles.
try:
    cursor.execute("create table Nivel\
      (ID_niveles INTEGER PRIMARY KEY AUTOINCREMENT,\
      Nivel TEXT not null,\
      Porcentaje_docente int)")

    print("La tabla Nivel fue creada correctamente")
except sqlite3.OperationalError as e:
    if str(e) == "table Nivel already exists":
        print("La tabla Nivel ya estaba creada")
    else:
        print("No se pudo crear la tabla Nivel")
        exit()

# Ahora creo la tabla de las materias.
try:
    cursor.execute("create table Materias\
      (ID_materias INTEGER PRIMARY KEY AUTOINCREMENT,\
      Materia TEXT not null,\
      ID_nivel int,\
      FOREIGN KEY(ID_nivel) REFERENCES Nivel(ID_niveles))")

    print("La tabla Materias fue creada correctamente")
except sqlite3.OperationalError as e:
    if str(e) == "table Materias already exists":
        print("La tabla Materias ya estaba creada")
    else:
        print("No se pudo crear la tabla Materias")
        print(e)
        exit()

# Ahora creo la tabla de las Aulas.
try:
    cursor.execute("create table Aulas\
      (ID_Aulas INTEGER PRIMARY KEY AUTOINCREMENT,\
      Nombre TEXT not null,\
       CLub_de_la_Tarea boolean not null)")

    print("La tabla Aulas fue creada correctamente")
except sqlite3.OperationalError as e:
    if str(e) == "table Aulas already exists":
        print("La tabla Aulas ya estaba creada")
    else:
        print("No se pudo crear la tabla Aulas")
        exit()

# Ahora creo la tabla de las Docentes-Materias.
try:
    cursor.execute("create table Docentes_y_Materias\
      (ID_doc_mat INTEGER PRIMARY KEY AUTOINCREMENT,\
      ID_mat int references Materias(ID_materias),\
      ID_doc int references Docentes(ID_docentes))")

    print("La tabla Docentes_y_Materias fue creada correctamente")
except sqlite3.OperationalError as e:
    if str(e) == "table Docentes_y_Materias already exists":
        print("La tabla Docentes_y_Materias ya estaba creada")
    else:
        print("No se pudo crear la tabla Docentes_y_Materias")
        print(e)
        exit()

# Ahora creo la tabla de las Cantidad de clases en el paquete.
try:
    cursor.execute("create table Cant_clas_por_paquete\
      (ID_cant_clas_por_paquete INTEGER PRIMARY KEY AUTOINCREMENT,\
      cantidad int)")

    print("La tabla Cant_clas_por_paquete fue creada correctamente")
except sqlite3.OperationalError as e:
    if str(e) == "table Cant_clas_por_paquete already exists":
        print("La tabla Cant_clas_por_paquete ya estaba creada")
    else:
        print("No se pudo crear la tabla Cant_clas_por_paquete")
        exit()

# Ahora creo la tabla de los costos de las clases.
try:
    cursor.execute("create table Costo_clase\
    (ID_costo_clase INTEGER PRIMARY KEY AUTOINCREMENT,\
    ID_cant_clas int references Cant_clas_por_paquete(ID_cant_clas_por_paquete),\
    particular boolean not null,\
    costo_total int)")

    print("La tabla Costo_clase fue creada correctamente")
except sqlite3.OperationalError as e:
    if str(e) == "table Costo_clase already exists":
        print("La tabla Costo_clase ya estaba creada")
    else:
        print("No se pudo crear la tabla Costo_clase")
        exit()

# Ahora creo la tabla de las clases.
try:
    cursor.execute("create table clases\
    (ID_clases INTEGER PRIMARY KEY AUTOINCREMENT,\
    ID_docente int references docentes(ID_docentes),\
    ID_materia int references materias(ID_materias),\
    ID_aula int references aulas(ID_aulas),\
    reprogramo boolean,\
    horario char(50))")

    print("La tabla clases fue creada correctamente")
except sqlite3.OperationalError as e:
    if str(e) == "table clases already exists":
        print("La tabla clases ya estaba creada")
    else:
        print("No se pudo crear la tabla clases")
        exit()

# Ahora creo la tabla de las alumnos_y_clases.
try:
    cursor.execute("create table alumnos_y_clases\
    (ID_alumnos_y_clases INTEGER PRIMARY KEY AUTOINCREMENT,\
    ID_alumno int references alumnos(ID_alumnos),\
    asistio boolean)")

    print("La tabla alumnos_y_clases fue creada correctamente")
except sqlite3.OperationalError as e:
    if str(e) == "table alumnos_y_clases already exists":
        print("La tabla alumnos_y_clases ya estaba creada")
    else:
        print("No se pudo alumnos_y_clases la tabla clases")
        exit()