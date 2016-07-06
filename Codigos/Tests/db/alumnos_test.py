import unittest
import datetime

from Codigos.Scripts_databases.Creo_databases import crear_db
from Codigos.Scripts_databases.Creo_databases import eliminar_db
from Codigos.Scripts_databases.Creo_databases import crear_tabla_alumnos

from Codigos.Scripts_databases.Operaciones_alumnos import *


class TestAlumnos(unittest.TestCase):

    def setUp(self):
        # Creo DB
        self.db = crear_db("test")

        # Creo tabla ALUMNOS utilizada para autenticación
        crear_tabla_alumnos(self.db)

    def tearDown(self):
        self.db.close()
        eliminar_db("test")

    # TEST 1: Poder agregar un alumno a la DB
    def test_1(self):
        self.assertTrue(agregar_alumno(self.db, "Arian", "Giles García",
                                       datetime.datetime(1991, 7, 13), 36201187,
                                       "arian2822@gmail.com", "2923-15-440464"))

    # TEST 2: Que el alumno agregado sea correctamente agregado a la DB
    def test_2(self):
        agregar_alumno(self.db, "Arian", "Giles García",
                       datetime.datetime(1991, 7, 13),
                       36201187,"arian2822@gmail.com",
                       "2923-15-440464")

        cursor = self.db.cursor()
        cursor.execute("SELECT count(*) FROM alumnos")
        count = cursor.fetchone()[0]

        self.assertEqual(count, 1)

    # TEST 3: Que el alumno pueda ser buscado por nombre
    def test_3(self):
        agregar_alumno(self.db, "Arian", "Giles García",
                       datetime.datetime(1991, 7, 13),
                       36201187,"arian2822@gmail.com",
                       "2923-15-440464")

        results = obtener_alumnos_por_nombre(self.db, "Giles García")

        self.assertNotEqual(results, [])

    # TEST 4: Que no encuentre alumnos que no existen
    def test_4(self):
        agregar_alumno(self.db, "Arian", "Giles García",
                       datetime.datetime(1991, 7, 13),
                       36201187,"arian2822@gmail.com",
                       "2923-15-440464")

        results = obtener_alumnos_por_nombre(self.db, "Arese")

        self.assertEqual(results, [])

    # TEST 5: Que se puedan buscar alumnos por DNI
    def test_5(self):
        agregar_alumno(self.db, "Arian", "Giles García",
                       datetime.datetime(1991, 7, 13),
                       36201187,"arian2822@gmail.com",
                       "2923-15-440464")

        results = obtener_alumnos_por_dni(self.db, 36201187)

        self.assertNotEqual(results, [])

    # TEST 6: Que se puedan buscar alumnos por DNI
    def test_6(self):
        agregar_alumno(self.db, "Arian", "Giles García",
                       datetime.datetime(1991, 7, 13),
                       36201187,"arian2822@gmail.com",
                       "2923-15-440464")

        results = obtener_alumnos_por_dni(self.db, 37615292)

        self.assertEqual(results, [])