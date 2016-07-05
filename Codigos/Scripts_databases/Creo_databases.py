import mysql.connector


def crear_db(name="academia"):
    db = mysql.connector.connect(user='root', password='root', host='127.0.0.1')
    cursor = db.cursor()

    try:
        cursor.execute("CREATE DATABASE {}".format(name))
        db.commit()
    except Exception as e:
        if str(e.args[0]) == str(1007):
            print("La base de datos academia ya estaba creada")
        else:
            print(e)

    db.close()
    db = mysql.connector.connect(user='root',password='root',host='127.0.0.1', database=name)

    return db


def crear_tabla_usuarios(db):
    cursor = db.cursor()

    try:
        cursor.execute("CREATE TABLE usuarios\
          (ID INTEGER PRIMARY KEY AUTO_INCREMENT,\
          username VARCHAR(100) NOT NULL UNIQUE,\
          password VARCHAR(100) NOT NULL,\
          privilegios INTEGER NOT NULL)")
        db.commit()

        print("La tabla Usuarios fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla Usuarios ya estaba creada")
        else:
            print(e)


def crear_root(db):
    cursor = db.cursor()

    try:
        cursor.execute("INSERT INTO usuarios\
          (username, password, privilegios)\
          VALUES('root', '4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2', 1)")
        print("El usuairo root se inserto correctamente")
        db.commit()
    except Exception as e:
        if str(e.args[0]) == str(1062):
            print("El usuario root ya esta creado")
        else:
            print(e)


def crear_tabla_alumnos(db):
    cursor = db.cursor()

    try:
        cursor.execute("create table Alumnos\
          (ID INTEGER PRIMARY KEY AUTO_INCREMENT,\
          Nombre VARCHAR(100) not null,\
          Apellido VARCHAR(100) not null,\
          Fecha_nacimiento VARCHAR(100),\
          DNI int not null,\
          Email VARCHAR(100),\
          Telefono VARCHAR(100))")
        db.commit()

        print("La tabla Alumnos fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla alumnos ya estaba creada")
        else:
            print(e)


def crear_tabla_docentes(db):
    cursor = db.cursor()

    try:
        cursor.execute("CREATE TABLE docentes\
          (ID INTEGER PRIMARY KEY AUTO_INCREMENT,\
           nombre VARCHAR(100) NOT NULL,\
           apellido VARCHAR(100) NOT NULL,\
           fecha_nacimiento VARCHAR(100),\
           dni INT NOT NULL,\
           email VARCHAR(100),\
           telefono VARCHAR(100))")
        db.commit()

        print("La tabla Docentes fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla docentes ya estaba creada")
        else:
            print(e)


def crear_tabla_niveles(db):
    cursor = db.cursor()

    try:
        cursor.execute("CREATE TABLE nivel\
          (id INTEGER PRIMARY KEY AUTO_INCREMENT,\
           nivel VARCHAR(100) NOT NULL,\
           porcentaje_docente INTEGER)")
        db.commit()

        print("La tabla Nivel fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla Niveles ya estaba creada")
        else:
            print(e)


def crear_tabla_materias(db):
    cursor = db.cursor()

    try:
        cursor.execute("CREATE TABLE materias\
          (id INTEGER PRIMARY KEY AUTO_INCREMENT,\
          materia VARCHAR(100) NOT NULL,\
          id_nivel INT REFERENCES nivel(id))")
        db.commit()

        print("La tabla Materias fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla materias ya estaba creada")
        else:
            print(e)


def crear_tabla_aulas(db):
    cursor = db.cursor()

    try:
        cursor.execute("CREATE TABLE aulas\
          (id INTEGER PRIMARY KEY AUTO_INCREMENT,\
           nombre VARCHAR(100) NOT NULL,\
           club_de_la_tarea BOOLEAN NOT NULL)")
        db.commit()

        print("La tabla Aulas fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla Aulas ya estaba creada")
        else:
            print(e)


def crear_tabla_docente_materia(db):
    cursor = db.cursor()

    try:
        cursor.execute("CREATE TABLE docentes_y_materias\
          (id INTEGER PRIMARY KEY AUTO_INCREMENT,\
           id_mat INTEGER REFERENCES materias(id),\
           id_doc INTEGER REFERENCES docentes(id))")
        db.commit()

        print("La tabla Docentes_y_Materias fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla Docentes-Materias ya estaba creada")
        else:
            print(e)


def crear_tabla_clase_paquete(db):
    cursor = db.cursor()

    try:
        cursor.execute("CREATE TABLE cant_clas_por_paquete\
          (id INTEGER PRIMARY KEY AUTO_INCREMENT,\
           cantidad INTEGER NOT NULL)")
        db.commit()

        print("La tabla Cant_clas_por_paquete fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla Cantidad de clases en el paquete ya estaba creada")
        else:
            print(e)


def crear_tabla_costo_clase(db):
    cursor = db.cursor()

    try:
        cursor.execute("CREATE TABLE costo_clase\
        (id INTEGER PRIMARY KEY AUTO_INCREMENT,\
        id_cant_clas INTEGER REFERENCES cant_clas_por_paquete(id),\
        particular BOOLEAN NOT NULL,\
        costo_total INTEGER,\
        costo_unitario INTEGER)")
        db.commit()

        print("La tabla Costo_clase fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla costos de las clases ya estaba creada")
        else:
            print(e)


def crear_tabla_clases(db):
    cursor = db.cursor()

    try:
        cursor.execute("CREATE TABLE clases\
        (id INTEGER PRIMARY KEY AUTO_INCREMENT,\
        id_docente INTEGER REFERENCES docentes(id),\
        id_materia INTEGER REFERENCES materias(id),\
        id_aula INTEGER REFERENCES aulas(ID),\
        id_costo_clases INTEGER REFERENCES costo_clase(id),\
        reprogramo BOOLEAN,\
        horario VARCHAR(100))")
        db.commit()

        print("La tabla clases fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla clases ya estaba creada")
        else:
            print(e)


def crear_tabla_alumnos_clases(db):
    cursor = db.cursor()

    try:
        cursor.execute("CREATE TABLE alumnos_y_clases\
        (id INTEGER PRIMARY KEY AUTO_INCREMENT,\
        id_alumno INTEGER REFERENCES alumnos(id),\
        id_clase INTEGER REFERENCES clases(id),\
        asistio BOOLEAN)")
        db.commit()

        print("La tabla alumnos_y_clases fue creada correctamente")
    except Exception as e:
        if str(e.args[0]) == str(1050):
            print("La tabla alumnos_y_clases ya estaba creada")
        else:
            print(e)


def crear_tablas():
    # Crear DB
    db = crear_db()

    # Crear tabla USUARIOS
    crear_tabla_usuarios(db)

    # Crear el usuario ROOT
    crear_root(db)

    # Crear tabla ALUMNOS
    crear_tabla_alumnos(db)

    # Crear tabla DOCENTES
    crear_tabla_docentes(db)

    # Crear tabla NIVELES
    crear_tabla_niveles(db)

    # Crear tabla MATERIAS
    crear_tabla_materias(db)

    # Crear tabla AULAS
    crear_tabla_aulas(db)

    # Crear tabla DOCENTE-MATERIA
    crear_tabla_docente_materia(db)

    # Crear tabla CANT-CLASES-POR-PAQUETE
    crear_tabla_clase_paquete(db)

    # Crear tabla COSTO-CLASE
    crear_tabla_costo_clase(db)

    # Crear tabla CLASES
    crear_tabla_clases(db)

    # Crear tabla ALUMNOS-CLASES
    crear_tabla_alumnos_clases(db)


def eliminar_db(name):
    db = mysql.connector.connect(user='root', password='root', host='127.0.0.1')
    cursor = db.cursor()

    try:
        cursor.execute("DROP DATABASE {}".format(name))
        db.commit()
    except Exception as e:
        if str(e.args[0]) == str(1007):
            print("La base de datos '{}' no existe o no se pudo eliminar".format(name))
        else:
            print(e)


class ErrorCrearTabla(Exception):
    def __str__(self):
        return "No se pudo crear la tabla, verifique las direcciones de las carpetas"


if __name__ == "__main__":
    crear_tablas()
    #eliminar_db("academia")




