import sqlite3

database = sqlite3.connect('C:\\Users\\JuanNotebook\\Documents\\GitHub\\Gestoin_academia\\Pruebas_sqlite3\\Databases\\prueba')

cursor = database.cursor()

print (u"la base de datos se abrio correctamente")

#creo una tabla
"""cursor.execute('''create table empresa
  (ID INT Primary key NOT NULL,
  Nombre TEXT not null,
  edad int not null,
  direccion char(50),
  salario real)''')"""

#print (u"tablad creada con exito")

#Inserto datos en la tabla.
'''cursor.execute("insert into empresa (id, nombre, edad, direccion, salario)\
               values (1,'Pablo', 32, 'montevideo', 20000.00)")


cursor.execute("insert into empresa (id, nombre, edad, direccion, salario)\
               values (2,'Alexis', 25, 'Maldonado', 15000.00)")


cursor.execute("insert into empresa (id, nombre, edad, direccion, salario)\
               values (3,'Diego', 29, 'San Jose', 20000.00)")

database.commit()

print (u"Se guardo correctamente.")'''

cursor.execute("select * from empresa")

for i in cursor:
    print("ID = ",i[0])
    print("Nombre = ", i[1])
    print("Direccion = ",i[2])
    print("Salario = ", i[3],"\n")

print("Operacion satisfactoria.")

database.close()