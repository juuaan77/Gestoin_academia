import sqlite3

def agregar_costo(db,id_cant_clases,particular,costo_total):

    #Primero obtengo el cursor de la db

    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
        cursor.execute("PRAGMA foreign_keys = ON")
        db.commit()
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo agregar_costo ->"+str(e))

    #Genero una consulta que me da la cantidad de clases correspondietes a el ID_cant_clases dado por parametros
    try:
        cursor.execute("select cantidad\
        from Cant_clas_por_paquete\
        where `ID_cant_clas_por_paquete` = ?",(id_cant_clases,))
        #Parceo la info obtenida en la consulta
        for i in cursor:
            cantidad = i[0]

        #print("La cantidad obtenida es: "+str(cantidad))
    except Exception as e:
        print("Error el obtener la cantidad por consulta en el metodo agregar_costo-> " + str(e))

    #Inserto un nuevo docente con los parametros dados.
    try:
        cursor.execute("INSERT INTO costo_clase\
          (ID_cant_clas,particular,costo_total,costo_unitario)\
          VALUES(?,?,?,?)",(id_cant_clases,particular,costo_total,costo_total/cantidad))
        print("El costo se inserto correctamente")
        # Comiteo los cambios a la base de datos.
        db.commit()
    except Exception as e:
        print("Error al insertar el costo, en el metodo agregar_costo -> " + str(e))


def eliminar_costo(db,key):

    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
        cursor.execute("PRAGMA foreign_keys = ON")
        db.commit()
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo eliminar_costo ->" + str(e))

    #Elimino el alumno correspondiente a la key dada.
    try:
        cursor.execute("DELETE FROM costo_clase where ID_costo_clase=?",(key,))
        print("El costo se elimino correctamente")
        # Comiteo los cambios a la base de datos.
        db.commit()
    except Exception as e:
        print("Error al eliminar un costo, en el metodo eliminar_costo -> " + str(e))


def actualizo_costo(db,key,costo_total):
    # Primero obtengo el cursor de la db
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
        cursor.execute("PRAGMA foreign_keys = ON")
        db.commit()
    except Exception as e:
        print("Error al abrir la base de datos, en el metodo actualizo_costo ->" + str(e))

    #Genero una consulta que me da la cantidad de clases correspondietes a la key
    try:
        cursor.execute("select cantidad\
        from Cant_clas_por_paquete\
        left outer join costo_clase\
        where ID_cant_clas = Id_cant_clas_por_paquete and id_costo_clase = ?",(key,))
        #Parceo la info obtenida en la consulta
        for i in cursor:
            cantidad = i[0]

        #print("La cantidad obtenida es: "+str(cantidad))
    except Exception as e:
        print("Error el obtener la cantidad por consulta en el metodo actualizo_costo-> " + str(e))

    # Actualizo el email del alumno correspondiente a la key dada.
    try:
        cursor.execute("UPDATE costo_clase set costo_total=?,costo_unitario=? where ID_costo_clase=?",\
                       (costo_total,costo_total/cantidad,key,))
        print("El costo se actualizo correctamente")
        # Comiteo los cambios a la base de datos.
        db.commit()
    except Exception as e:
        print("Error al actualizar un costo, en el metodo actualizo_costo -> " + str(e))


if __name__ == "__main__":
    database = sqlite3.connect('..\\..\\Databases\\Academia.db')
    #agregar_costo(database,2,True,200)
    #agregar_costo(database, 2, False, 100)
    #eliminar_costo(database,1)
    #actualizo_costo(database,4,400)
    database.close()