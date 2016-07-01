import sqlite3


#Primero creo la base de datos.
database = sqlite3.connect('C:\\Users\\JuanNotebook\\Documents\\GitHub\\Gestoin_academia\\Databases\\Academi.db')

cursor = database.cursor()

print (u"la base de datos se creo correctamente")

#Creo las tablas.
try:
    cursor.execute("create table Alumnos\
      (ID INT Primary key NOT NULL,\
      \"Nombre y Apellido\" TEXT not null,\
      Edad int not null,\
      DNI int not null,\
      Email char(50),\
      Telefono char(50))")
except sqlite3.OperationalError as e:
    if str(e) == "table Alumnos already exists":
        print("La tabla ya fue creada")
    else:
        print("No se pudo crear la tabla")
        exit()


#print("Creo la tabla")

