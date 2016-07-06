import unittest

from Codigos.Scripts_databases.Creo_databases import crear_db
from Codigos.Scripts_databases.Creo_databases import eliminar_db
from Codigos.Scripts_databases.Creo_databases import crear_tabla_alumnos_clases

from Codigos.Scripts_databases.Operaciones_Alumnos_y_clases import agregar_alumno_y_clase
from Codigos.Scripts_databases.Operaciones_Alumnos_y_clases import ErrorAgregarAlumnoClase


class TestAlumnosClases(unittest.TestCase):

    def setUp(self):
        # Creo DB
        self.db = crear_db("test")

        # Creo tabla ALUMNOS-CLASES
        crear_tabla_alumnos_clases(self.db)

    def tearDown(self):
        self.db.close()
        eliminar_db("test")

    # TEST 1: Poder agregar un alumno/clase a la tabla
    def test_1(self):
        self.assertTrue(agregar_alumno_y_clase(self.db, 1, 1))

    # TEST 2: No poder agregar un alumno/clase a la tabla con parámetros incorrectos
    def test_2(self):
        self.assertRaises(ErrorAgregarAlumnoClase, agregar_alumno_y_clase, self.db, "asd", 1)