import mysql.connector


def agregar_alumno_y_clase(db,id_alumno,id_clase):
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo agregar_alumno_y_clase ->"+str(e))

    # Inserto un nuevo alumno/clase con los parametros dados.
    try:
        cursor.execute("INSERT INTO alumnos_y_clases\
          (id_alumno,id_clase)\
          VALUES({},{})".format(id_alumno,id_clase))
        print("El alumno y clase se inserto correctamente")
        db.commit()

        return True
    except Exception as e:
        raise ErrorAgregarAlumnoClase


class ErrorAgregarAlumnoClase(Exception):
    def __str__(self):
        return "No se pudo agregar el alumno/clase"


if __name__ == "__main__":
    database = mysql.connector.connect(user='root', password='root', host='127.0.0.1',database='academia')
    database.close()