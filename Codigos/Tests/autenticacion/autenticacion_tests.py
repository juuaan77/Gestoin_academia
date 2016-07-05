import unittest

from Codigos.Autenticacion.autenticacion import Autenticador, ErrorAutenticacion, ErrorFormatoClave
from Codigos.Scripts_databases.Creo_databases import crear_db
from Codigos.Scripts_databases.Creo_databases import eliminar_db
from Codigos.Scripts_databases.Creo_databases import crear_tabla_usuarios
from Codigos.Scripts_databases.Creo_databases import crear_root


class TestAutenticacion(unittest.TestCase):

    def setUp(self):
        # Creo DB
        self.db = crear_db("test")

         # Creo tabla USUARIOS utilizada para autenticación
        crear_tabla_usuarios(self.db)

        # Creo usuario ROOT-ROOT en la tabla USUARIO
        crear_root(self.db)

        # Creo AUTENTICADOR
        self.auth = Autenticador(self.db)

    def tearDown(self):
        self.db.close()
        eliminar_db("test")

    # TEST 1: Poder autenticarse con el usuario por defecto (root/root)
    def test_1(self):
        result = self.auth.autenticar("root", "root")
        self.assertTrue(result)

    # TEST 2: No poder autenticarse con el usuario por defecto con otra contraseña
    def test_2(self):
        self.assertRaises(ErrorAutenticacion, self.auth.autenticar, "root", "123")

    # TEST 3: No poder autenticarse con un usuario que no existe
    def test_3(self):
        self.assertRaises(ErrorAutenticacion, self.auth.autenticar, "user", "pass")

    # TEST 4: No poder autenticarse con un usuario que no existe
    def test_4(self):
        self.assertRaises(ErrorAutenticacion, self.auth.autenticar, "user", "pass")

    # TEST 5: Que el usuario root no pueda crear un usuario con clave pobre
    def test_5(self):
        self.auth.autenticar("root", "root")
        self.assertRaises(ErrorFormatoClave, self.auth.crear_usuario, "docente", "soydocente", 3)

    # TEST 6: Que el usuario root pueda crear un usuario con clave válida
    def test_6(self):
        self.auth.autenticar("root", "root")
        self.assertTrue(self.auth.crear_usuario("docente", "Docente123", 3))

    # TEST 7: Que el usuario docente no pueda cambiar su clave por una clave pobre
    def test_7(self):
        self.auth.autenticar("root", "root")
        self.auth.crear_usuario("docente", "Docente123", 3)
        self.auth.desautenticar()

        self.auth.autenticar("docente", "Docente123")
        self.assertRaises(ErrorFormatoClave, self.auth.cambiar_clave, "docente")

    # TEST 8: Que el usuario docente pueda cambiar su clave por una clave válida
    def test_8(self):
        self.auth.autenticar("root", "root")
        self.auth.crear_usuario("docente", "Docente123", 3)
        self.auth.desautenticar()

        self.auth.autenticar("docente", "Docente123")
        self.assertTrue(self.auth.cambiar_clave("OtraPass45"))

    # TEST 9: Que el cambio de clave se realice correctamente
    def test_9(self):
        self.auth.autenticar("root", "root")
        self.auth.crear_usuario("docente", "Docente123", 3)
        self.auth.desautenticar()

        self.auth.autenticar("docente", "Docente123")
        self.auth.cambiar_clave("OtraPass45")
        self.auth.desautenticar()

        self.assertTrue(self.auth.autenticar("docente", "OtraPass45"))