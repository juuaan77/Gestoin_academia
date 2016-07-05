import mysql.connector

def agregar_materia(db,materia,id_nivel):

    #Primero obtengo el cursor de la db

    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
        cursor.execute("PRAGMA foreign_keys = ON")
        db.commit()
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo agregar_materia ->"+str(e))

    #Inserto un nuevo docente con los parametros dados.
    try:
        cursor.execute("INSERT INTO materias\
          (materia,ID_nivel)\
          VALUES('{}',{})".format(materia,id_nivel,))
        print("La materia se inserto correctamente")
        db.commit()
    except Exception as e:
        print("Error al insertar una materia, en el metodo agregar_materia -> " + str(e))

    #Comiteo los cambios a la base de datos.

if __name__ == "__main__":
    database = mysql.connector.connect(user='root', password='root', host='127.0.0.1',database='academia')
    database.close()