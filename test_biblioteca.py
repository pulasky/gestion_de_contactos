import unittest
from Sistema_de_gestion_de_biblioteca import Libro, Biblioteca

class TestBiblioteca(unittest.TestCase):

    def setUp(self):
        self.biblioteca = Biblioteca()
        self.libro = Libro("Título de prueba", "Autor de prueba", "1234567890")
        self.biblioteca.libros.append(self.libro)

    def test_agregar_libro(self):
        self.biblioteca.agregar()
        self.assertEqual(len(self.biblioteca.libros), 2)

    def test_prestar_libro(self):
        self.biblioteca.prestar()
        self.assertFalse(self.libro.disponible)

    def test_devolver_libro(self):
        self.libro.disponible = False
        self.biblioteca.devolver()
        self.assertTrue(self.libro.disponible)

    def test_mostrar_libros(self):
        self.biblioteca.mostrar()
        self.assertEqual(len(self.biblioteca.libros), 1)

    def test_buscar_libro(self):
        self.biblioteca.buscar()
        self.assertEqual(self.libro.isbn, "1234567890")

if __name__ == "__main__":
    unittest.main()