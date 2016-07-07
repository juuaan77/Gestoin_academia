import unittest

from Codigos.Scripts_databases.Creo_databases import crear_db
from Codigos.Scripts_databases.Creo_databases import eliminar_db
from Codigos.Scripts_databases.Creo_databases import crear_tabla_aulas

from Codigos.Scripts_databases.Operaciones_aulas import agregar_aula
from Codigos.Scripts_databases.Operaciones_aulas import ErrorAgregarAula


class TestAulas(unittest.TestCase):

    def setUp(self):
        # Creo DB
        self.db = crear_db("test")

        # Creo tabla AULAS
        crear_tabla_aulas(self.db)

    def tearDown(self):
        self.db.close()
        eliminar_db("test")

    # TEST 1: Poder agregar un aula a la tabla
    def test_1(self):
        self.assertTrue(agregar_aula(self.db, "Aula Magna", False))

    # TEST 2: Que el aula agregado sea correctamente agregado a la DB
    def test_2(self):
        agregar_aula(self.db, "Aula Magna", False)

        cursor = self.db.cursor()
        cursor.execute("SELECT count(*) FROM aulas")
        count = cursor.fetchone()[0]

        self.assertEqual(count, 1)

    # TEST 3: No poder agregar un aula a la tabla con parámetros incorrectos
    def test_3(self):
        self.assertRaises(ErrorAgregarAula, agregar_aula, self.db, "Aula Magna", "No")