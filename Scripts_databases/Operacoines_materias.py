import sqlite3

def agregar_materia(db,materia,id_nivel):

    #Primero obtengo el cursor de la db

    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo agregar_materia ->"+str(e))

    #Inserto un nuevo docente con los parametros dados.
    try:
        cursor.execute("INSERT INTO docentes\
          (Nombre_y_Apellido, Edad, DNI, Email, Telefono)\
          VALUES(?,?,?,?,?)",valores)
        print("El docente se inserto correctamente")
    except Exception as e:
        print("Error al insertar un docente, en el metodo agregar docente -> " + str(e))

    #Comiteo los cambios a la base de datos.
    db.commit()

def eliminar_docente(db,key):

    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo eliminar docente ->" + str(e))

    #Elimino el alumno correspondiente a la key dada.
    try:
        cursor.execute("DELETE FROM docentes where ID_docentes=?",(key,))
        print("El docente se elimino correctamente")
    except Exception as e:
        print("Error al eliminar un docente, en el metodo agregar docente -> " + str(e))

    #Comiteo los cambios a la base de datos.
    db.commit()

if __name__ == "__main__":
    database = sqlite3.connect('C:\\Users\\JuanNotebook\\Documents\\GitHub\\Gestoin_academia\\Databases\\Academia.db')

    #agregar_docente(database,"juan arese",23,36935267,"juan_arese@hotmail.com","3564524759")
    eliminar_docente(database,1)
    database.close()