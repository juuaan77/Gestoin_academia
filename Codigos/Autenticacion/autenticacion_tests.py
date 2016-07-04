import unittest
import sqlite3
import os

from autenticacion import Autenticador
from autenticacion import ErrorFormatoClave
from autenticacion import ErrorEliminarUsuario


class AutenticacionTests(unittest.TestCase):

    def setUp(self):
        """
        La base de datos debe tener un usuario "r" con contraseña "root" y nada mas
        """
        self.db = sqlite3.connect('db_test.db')
        self.cursor = self.db.cursor()

        #Primero creo la tabla de usuarios.
        try:
            self.cursor.execute("create table Usuarios\
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
            self.cursor.execute("INSERT INTO Usuarios\
              (username,password,privilegios)\
              VALUES('root','4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2',1)")
            print("El usuairo root se inserto correctamente")
            self.db.commit()
        except Exception as e:
            print("Error al crear el usuario root, en el modulo creo_databases -> " + str(e))

            #Comiteo los cambios a la base de datos.
            self.db.commit()

        self.auth = Autenticador(self.db)

    def tearDown(self):
        self.db.close()
        try:
            os.remove("db_test.db")
        except:
            pass

    def test_1(self):
        """
        Prueba que se pueda acceder como root root.
        """
        self.assertTrue(self.auth.autenticar("root", "root"))

    def test_2(self):
        """
        Prueba que la contraseña no puede ser menor a 8 dígitos, etc.
        """
        self.auth.autenticar("root", "root")
        self.assertRaises(ErrorFormatoClave, self.auth.crear_usuario, "docente", "doc", 3)

    def test_3(self):
        """
        Prueba que root puede crear un usuario llamado docente
        """
        self.auth.autenticar("root", "root")
        self.assertTrue(self.auth.crear_usuario("docente", "Docente123", 3))

    def test_4(self):
        """
        Prueba que el docente pueda cambiar su contraseña
        """
        self.auth.autenticar("docente", "Docente123")
        self.assertTrue(self.auth.cambiar_clave("SoyDocente456"))

    def test_5(self):
        """
        Prueba que el docente pueda loguearse con su nueva contraseña
        """
        self.assertTrue(self.auth.autenticar("docente", "SoyDocente456"))

    def test_6(self):
        """
        Prueba que el docente no puede borrar al root
        """
        self.auth.autenticar("docente", "SoyDocente456")
        self.assertRaises(ErrorEliminarUsuario, self.auth.eliminar_usuario, "root")

    def test_7(self):
        """
        Prueba que el root puede eliminar al usuario docente
        """
        self.auth.autenticar("root", "root")
        self.assertTrue(self.auth.eliminar_usuario("docente"))


if __name__ == '__main__':
    unittest.main()
