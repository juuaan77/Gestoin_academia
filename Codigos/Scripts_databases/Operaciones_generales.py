import sqlite3

def obtengo_cursor(db):
    try:
        cursor = db.cursor()
        print("la base de datos se abrio correctamente")
        return cursor
    except Exception as e:
        raise ErrorObtencionCursor

def obtener_fila(db,tabla,key):
    #primero obtengo el cursor
    cursor = obtengo_cursor(db)

    try:
        cursor.execute("select *\
                        from {}\
                       where ID={}".format(tabla,key))

        for i in cursor:
            fila = i
        return fila
    except Exception as e:
        raise ErrorRealizarConsulta

def eliminar_fila(db,tabla,key):
    # primero obtengo el cursor
    cursor = obtengo_cursor(db)

    #Elimino la fila
    try:
        cursor.execute("delete from {}\
                        where ID={}".format(tabla, key))
        # Comiteo los cambios a la base de datos.
        db.commit()
        print("La fila se elimino correctamente")
    except Exception as e:
        raise ErrorEliminarFila

def actualizo_atributo(db,key,tabla,atributo,valor):
    # primero obtengo el cursor
    cursor = obtengo_cursor(db)

    try:
        cursor.execute("update {}\
                        set {}='{}'\
                       where ID={}".format(tabla,atributo,valor,key))
        db.commit()
    except Exception as e:
        print("Error al actualizar el atributo->",str(e))

class ErrorObtencionCursor(Exception):
    def __str__(self):
        return "No se pudo obtener el cursor, verifique que el parametro \"basededatos\" es correcto y que la db esta conectada."

class ErrorRealizarConsulta(Exception):
    def __str__(self):
        return "No se pudo realizar la consulta, verifique que los parametros son los adecuados."

class ErrorEliminarFila(Exception):
    def __str__(self):
        return "No se pudo eliminar la fila, revise los parametros."

if __name__ == "__main__":
    database = sqlite3.connect('..\\..\\Databases\\Academia.db')
    actualizo_atributo(database,1,"alumnos","apellido","bernard")
    database.close()