"""Se crea una clase Libro con los 
atributos titulo (str), autor (str), isbn (str) y disponible (bool, 
inicialmente True)"""
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    """El método mostrar deberá mostrar por pantalla 
    los datos del libro."""
    def mostrar(self):
        estado = "Disponible" if self.disponible else "No disponible"
        print("-" * 25)
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("ISBN:", self.isbn)
        print("Estado:", estado)
        

    """El método prestar deberá cambiar el atributo disponible a False
    y dar un mensaje sobre la gestión."""
    
    def prestar(self):
        if self.disponible:
            self.disponible = False
            print("\nEl préstamo se ha gestionado correctamente.")
        else:
            print("\nEl libro no está disponible.")

    """El método devolver deberá cambiar el atributo disponible a True
    y dar un mensaje sobre la gestión."""

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print("\nLa devolución se ha gestionado correctamente.")
        else:
            print("\nEl libro ya estaba en la biblioteca.")

"""Se crea una clase Biblioteca con un atributo libros que será una 
lista de objetos de la clase Libro."""

class Biblioteca:
    def __init__(self):
        self.libros = []

    """El método agregar deberá añadir un libro a la lista de libros."""

    def agregar(self):
        
        titulo = input("Por favor, introduce el título del libro: ")
        while len(titulo.strip()) == 0:
            print("\nNo se ha introducido ningún título.")
            titulo = input("Por favor, introduce el título del libro: ")        
        
        autor = input("Por favor, introduce el autor del libro: ")
        while len(autor.strip()) == 0:
            print("\nNo se ha introducido ningún autor.")
            autor = input("Por favor, introduce el autor del libro: ")
        
        isbn = input("Por favor, introduce el ISBN del libro: ")
        while len(isbn.strip()) == 0:
            print("\nNo se ha introducido ningún ISBN.")
            isbn = input("Por favor, introduce el ISBN del libro: ")
        
        """Comprueba si el ISBN ya existe en la biblioteca."""

        for libro in self.libros:
            if libro.isbn == isbn:
                print("\nEl ISBN ya existe en la biblioteca.")
                return              
        
        libro = Libro(titulo, autor, isbn)
        self.libros.append(libro)
        print("\nLibro añadido correctamente.")

    """El método prestar deberá recibir el ISBN de un libro y dar
    un mensaje de error si el libro no está en la biblioteca"""

    def prestar(self):
        isbn = input("\nPor favor, introduce el ISBN del libro a prestar: ")
        for libro in self.libros:
            if libro.isbn == isbn:
                libro.prestar()
                return
        print("\nLibro no encontrado.")

    """El método devolver deberá recibir el ISBN de un libro y dar
    un mensaje de error si el libro no está en la biblioteca"""  

    def devolver(self):
        isbn = input("\nPor favor,introduce el ISBN del libro a devolver: ")
        for libro in self.libros:
            if libro.isbn == isbn:
                libro.devolver()
                return
        print("\nLibro no encontrado.")

    """El método mostrar muestra por pantalla el número de libros que hay
    (error si es 0) y los datos de todos los libros de la biblioteca."""

    def mostrar(self):
        print("Número de libros:", len(self.libros))
        print("-" * 25)
        if len(self.libros) == 0:
                print("\nNo hay libros en la biblioteca.")
                return
        print("Catálogo de libros:")
        for libro in self.libros:
            libro.mostrar()
        
    """El método buscar deberá recibir el ISBN de un libro y mostrar
    por pantalla los datos de ese libro."""

    def buscar(self):
        isbn = input("\nPor favor, introduce el ISBN del libro: ")
        for libro in self.libros:
            if libro.isbn == isbn:
                libro.mostrar()
                return
        print("\nLibro no encontrado.")

    """El método menu deberá mostrar un menú con las siguientes opciones:
    1. Agregar libro
    2. Prestar libro
    3. Devolver libro
    4. Mostrar libros
    5. Buscar libro
    6. Salir del programa
    El método deberá ejecutar la opción seleccionada o error si no es válida."""
    
    def menu(self):
        while True:
            print("-" * 25)
            print("Bienvenido al sistema de gestión de biblioteca.\n")          
            print("1. Agregar libro")
            print("2. Prestar libro")
            print("3. Devolver libro")
            print("4. Mostrar libros")
            print("5. Buscar libro")
            print("6. Salir del programa\n")
            opcion = input("Por favor, introduce una opción: ")
            print("-" * 25)
            if opcion == "1":
                self.agregar()
            elif opcion == "2":
                self.prestar()
            elif opcion == "3":
                self.devolver()
            elif opcion == "4":
                self.mostrar()
            elif opcion == "5":
                self.buscar()
            elif opcion == "6":
                break
            else:
                print("\nOpción no válida. Intruduce un número del 1 al 6.")

""" Se crea un objeto de la clase Biblioteca y se ejecuta el método menu."""

if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.menu()