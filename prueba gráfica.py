import tkinter as tk
from tkinter import messagebox

# Función que se ejecuta al hacer clic en el botón
def on_button_click():
    messagebox.showinfo("Información", "¡Has hecho clic en el botón!")

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana de Ejemplo")
root.geometry("300x200")

# Crear un botón y añadirlo a la ventana
button = tk.Button(root, text="Haz clic aquí", command=on_button_click)
button.pack(pady=20)

# Iniciar el bucle principal de la ventana
root.mainloop()