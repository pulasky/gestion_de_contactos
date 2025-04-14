"""Este progama simula un sistema de gestión de contactos.
   El programa permite al usuario agregar, eliminar,
   buscar y mostrar todos los contactos en una lista.
   Los contactos se guardan en un archivo de texto.
   El programa utiliza un menú para que el usuario pueda
   seleccionar la opción deseada.
   Se creará una clase Contacto que contendrá los atributos
   nombre, apellidos, teléfono y correo electrónico.
   Se creará una clase GestionContactos que contenga una 
   lista de contactos y métodos para agregar, mostrar, buscar,
   eliminar y actualizar contactos."""

"""Importar la librería re para expresiones regulares. (Validación de email)"""
import re  

class Contacto:
    def __init__(self, nombre, apellidos, telefono, email):
        
        """Validar que el nombre o apellidos no admitan campos vacíos. 
        El número de teléfono debe tener 9 dígitos y el correo electrónico tiene
        que tener un formato correcto. Si no se cumplen estas condiciones, 
        se lanza una excepción ValueError."""
    
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
    
        if not apellidos.strip():
            raise ValueError("Los apellidos no pueden estar vacíos")
        
        if len(telefono) != 9 or not telefono.isdigit():
            raise ValueError("Número de teléfono inválido. Debe tener 9 dígitos.")
            
        patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron_email, email):
            raise ValueError("Formato de email inválido. Debe ser ejemplo@dominio.com")

        """Asignar los valores a los atributos de la clase.
           Se eliminan los espacios en blanco al principio y al final
           de los nombres y apellidos."""
        
        self.nombre = nombre.strip()
        self.apellidos = apellidos.strip()
        self.telefono = telefono
        self.email = email

    """Método para representar el contacto como una cadena.
       Devuelve una cadena con el nombre, apellidos, 
       teléfono y correo electrónico."""
    
    def __str__(self):
        return f"{self.nombre}, {self.apellidos}, {self.telefono}, {self.email}"

    
class GestionContactos:
    def __init__(self):
        self.contactos = []
        self.archivo = "contactos.txt"
        self.cargar_contactos()

    """Método para agregar un nuevo contacto.
       Crea un nuevo objeto Contacto y lo añade a la lista de contactos."""
    
    def agregar_contacto(self, nombre, apellidos, telefono, email):
        try:
            nuevo_contacto = Contacto(nombre, apellidos, telefono, email)
            self.contactos.append(nuevo_contacto)
            self.guardar_contactos()
            print("Contacto agregado correctamente.")
            return True
        except ValueError as e:
            print(f"Error al agregar contacto: {e}")
            return False

    """Método para buscar un contacto por nombre.
       Busca en la lista de contactos y muestra los detalles"""
    
    def buscar_contacto(self, nombre):
        contactos_encontrados = [c for c in self.contactos if c.nombre.lower() == nombre.lower()]
        if contactos_encontrados:
            for contacto in contactos_encontrados:
                print(contacto)
            return True
        print("Contacto no encontrado.")
        return False

    """Método para eliminar un contacto por nombre.
       Busca en la lista de contactos y elimina el contacto"""
    
    def eliminar_contacto(self, nombre):
        
        """Encontrar todos los contactos con el mismo nombre 
              (ignorando mayúsculas y minúsculas)"""
        
        contactos_encontrados = [c for c in self.contactos if c.nombre.lower() == nombre.lower()]
        
        if not contactos_encontrados:
            print("Contacto no encontrado.")
            return False
            
        if len(contactos_encontrados) == 1:
            self.contactos.remove(contactos_encontrados[0])
            self.guardar_contactos()
            print("Contacto eliminado correctamente.")
            return True
        
        """Si hay múltiples contactos, mostrar opciones
              y permitir al usuario seleccionar cuál eliminar"""
        
        print("\nSe encontraron varios contactos con ese nombre:")
        for i, contacto in enumerate(contactos_encontrados, 1):
            print(f"{i}. {contacto}")
        
        try:
            while True:
                seleccion = int(input("\nSeleccione el número del contacto a eliminar (0 para cancelar): "))
                if seleccion == 0:
                    print("Operación cancelada.")
                    return False
                if 1 <= seleccion <= len(contactos_encontrados):
                    self.contactos.remove(contactos_encontrados[seleccion - 1])
                    self.guardar_contactos()
                    print("Contacto eliminado correctamente.")
                    return True
                print("Selección inválida. Por favor, intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Debe introducir un número.")
            return False

    """Método para actualizar un contacto por nombre.
       Busca en la lista de contactos y actualiza los detalles"""
    
    def actualizar_contacto(self, nombre_buscar, nombre_nuevo, apellidos, telefono, email):
        contactos_encontrados = [c for c in self.contactos if c.nombre.lower() == nombre_buscar.lower()]
        
        if not contactos_encontrados:
            print("Contacto no encontrado.")
            return False
            
        if len(contactos_encontrados) == 1:
            indice = self.contactos.index(contactos_encontrados[0])
        else:
            print("\nSe encontraron varios contactos con ese nombre:")
            for i, contacto in enumerate(contactos_encontrados, 1):
                print(f"{i}. {contacto}")
            
            try:
                while True:
                    seleccion = int(input("\nSeleccione el número del contacto a actualizar (0 para cancelar): "))
                    if seleccion == 0:
                        print("Operación cancelada.")
                        return False
                    if 1 <= seleccion <= len(contactos_encontrados):
                        indice = self.contactos.index(contactos_encontrados[seleccion - 1])
                        break
                    print("Selección inválida. Por favor, intente de nuevo.")
            except ValueError:
                print("Entrada inválida. Debe introducir un número.")
                return False
        
        try:
            nuevo_contacto = Contacto(nombre_nuevo, apellidos, telefono, email)
            self.contactos[indice] = nuevo_contacto
            self.guardar_contactos()
            print("Contacto actualizado correctamente.")
            return True
        except ValueError as e:
            print(f"Error al actualizar contacto: {e}")
            return False

    """Método para mostrar todos los contactos.
       Recorre la lista de contactos y los imprime uno por uno."""
    
    def mostrar_todos_contactos(self):
        if not self.contactos:
            print("No hay contactos guardados.")
            return False
        
        try:
            """Calcular el ancho de cada columna
               para alinear la tabla"""
            
            ancho_nombre = max(max(len(c.nombre) for c in self.contactos), len('Nombre'))
            ancho_apellidos = max(max(len(c.apellidos) for c in self.contactos), len('Apellidos'))
            ancho_telefono = 9  # Siempre es 9
            ancho_email = max(max(len(c.email) for c in self.contactos), len('Email'))

            """Crear una línea de separación
               con el ancho total de la tabla"""
            
            linea = "─" * (ancho_nombre + ancho_apellidos + ancho_telefono + ancho_email + 13)

            """Imprimir encabezados de la tabla
               con los nombres de las columnas"""
            
            print(linea)
            print(f"│ {'Nombre':<{ancho_nombre}} │ {'Apellidos':<{ancho_apellidos}} │ {'Teléfono':<9} │ {'Email':<{ancho_email}} │")
            print(linea)

            """Recorrer la lista de contactos
               e imprimir cada uno en una fila de la tabla"""
            
            for contacto in self.contactos:
                print(f"│ {contacto.nombre:<{ancho_nombre}} │ {contacto.apellidos:<{ancho_apellidos}} │ {contacto.telefono:<9} │ {contacto.email:<{ancho_email}} │")
            
            print(linea)
            return True

        except Exception as e:
            print(f"Error al mostrar contactos: {e}")
            return False

    """ Método para cargar contactos desde un archivo.
        Lee el archivo de contactos y crea objetos Contacto"""
    
    def cargar_contactos(self):
        try:
            """Abrir el archivo de contactos en modo lectura
               y leer cada línea del archivo. Intenta primero con
               la codificación 'utf-8', y si falla, intenta con 'latin-1'"""
            
            try:
                with open(self.archivo, "r", encoding='utf-8') as f:
                    self._leer_contactos(f)
            except UnicodeDecodeError:
                # Si falla, intentar con otra codificación
                with open(self.archivo, "r", encoding='latin-1') as f:
                    self._leer_contactos(f)
        except FileNotFoundError:
            print("Archivo de contactos no encontrado. Creando nuevo archivo.")
            open(self.archivo, "w", encoding='utf-8').close()
        except PermissionError:
            print("Error: No hay permisos para acceder al archivo.")
        except Exception as e:
            print(f"Error inesperado al abrir el archivo: {e}")

    """Método privado para leer contactos desde un archivo.
       Se utiliza para evitar la duplicación de código"""
    
    def _leer_contactos(self, f):
        for linea in f:
            try:
                nombre, apellidos, telefono, email = linea.strip().split(", ")
                contacto = Contacto(nombre, apellidos, telefono, email)
                self.contactos.append(contacto)
            except ValueError as e:
                print(f"Error al cargar contacto: {e}")
            except Exception as e:
                print(f"Error inesperado al cargar contacto: {e}")

    """Método para guardar contactos en un archivo.
       Recorre la lista de contactos y los escribe en el archivo"""
    
    def guardar_contactos(self):
        try:
            with open(self.archivo, "w", encoding='utf-8', newline='') as f:
                for contacto in self.contactos:
                    f.write(f"{contacto}\n")
            return True
        except PermissionError:
            print("Error: No hay permisos para escribir en el archivo.")
            return False
        except IOError as e:
            print(f"Error de E/S al guardar contactos: {e}")
            return False
        except Exception as e:
            print(f"Error inesperado al guardar contactos: {e}")
            return False

"""Función principal que ejecuta el programa.
   Muestra un menú al usuario y llama a los métodos de la clase GestionContactos"""

def main():
    gestion = GestionContactos()
    
    def validar_y_buscar():
        if not gestion.contactos:
            print("No hay contactos guardados.")
            return False
        return gestion.buscar_contacto(input("Nombre a buscar: "))
    
    def validar_y_eliminar():
        if not gestion.contactos:
            print("No hay contactos guardados.")
            return False
        return gestion.eliminar_contacto(input("Nombre a eliminar: "))
    
    def validar_y_actualizar():
        if not gestion.contactos:
            print("No hay contactos guardados.")
            return False
        return gestion.actualizar_contacto(
            input("Nombre del contacto a buscar: "),
            input("Nuevo nombre: "),
            input("Nuevos apellidos: "),
            input("Nuevo teléfono: "),
            input("Nuevo email: "))
    
    menu_opciones = {
        "1": ("Agregar contacto", lambda: gestion.agregar_contacto(
            input("Nombre: "), input("Apellidos: "),
            input("Teléfono: "), input("Email: "))),
        "2": ("Mostrar contactos", gestion.mostrar_todos_contactos),
        "3": ("Buscar contacto", validar_y_buscar),
        "4": ("Eliminar contacto", validar_y_eliminar),
        "5": ("Actualizar contacto", validar_y_actualizar),
        "6": ("Salir", lambda: True)
    }

    while True:
        print("\n--- Menú de Gestión de Contactos ---")
        for key, (nombre, _) in menu_opciones.items():
            print(f"{key}. {nombre}")

        opcion = input("\nSeleccione una opción: ")
        if opcion not in menu_opciones:
            print("Opción inválida")
            continue

        if opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            menu_opciones[opcion][1]()

if __name__ == "__main__":
    main()
# Fin del programa
