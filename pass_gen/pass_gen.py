"""
Genera una contraseña aleatoria en función de los valores introducidos por el usuario.
"""

import tkinter as tk
import string
import random
from tkinter import messagebox
from PIL import Image, ImageTk

def generar_contraseña():
    try:
        longitud = int(entry_longitud.get())
        if longitud < 1:
            raise ValueError("La longitud debe ser mayor que 0")
    except ValueError:
        messagebox.showerror("Error", "Introduce una longitud válida para la contraseña.")
        return

    opciones = ""
    caracteres_seleccionados = []

    # Añadir un carácter de cada tipo seleccionado
    if var_mayus.get():
        opciones += string.ascii_uppercase
        caracteres_seleccionados.append(random.choice(string.ascii_uppercase))
    if var_minus.get():
        opciones += string.ascii_lowercase
        caracteres_seleccionados.append(random.choice(string.ascii_lowercase))
    if var_numeros.get():
        opciones += string.digits
        caracteres_seleccionados.append(random.choice(string.digits))
    if var_especial.get():
        opciones += string.punctuation
        caracteres_seleccionados.append(random.choice(string.punctuation))

    if not opciones:
        messagebox.showerror("Error", "Selecciona al menos una opción")
        return

    # Generar el resto de la contraseña de forma aleatoria
    while len(caracteres_seleccionados) < longitud:
        caracteres_seleccionados.append(random.choice(opciones))

    # Mezclar los caracteres seleccionados para mayor aleatoriedad
    random.shuffle(caracteres_seleccionados)

    # Convertir la lista en cadena y mostrar la contraseña generada
    contraseña = ''.join(caracteres_seleccionados)
    entry_contraseña.delete(0, tk.END)
    entry_contraseña.insert(0, contraseña)

def copiar_contraseña():
    contraseña = entry_contraseña.get()
    if contraseña:
        ventana.clipboard_clear()
        ventana.clipboard_append(contraseña)
        mostrar_mensaje_copiado()

def mostrar_mensaje_copiado():
    label_copiado.config(text="¡Contraseña copiada!")
    ventana.after(2000, ocultar_mensaje_copiado)  # Ocultar el mensaje después de 2 segundos

def ocultar_mensaje_copiado():
    label_copiado.config(text="")

def mostrar_menu_contextual(event):
    menu_contextual.post(event.x_root, event.y_root)

def toggle_opcion(opcion, boton):
    if opcion.get():
        opcion.set(False)
        boton.config(text="", bg="lightgray", fg="black")  # Cambiar el fondo cuando no está seleccionado
    else:
        opcion.set(True)
        boton.config(text="✔", bg="lightgreen", fg="green")  # Mostrar el tick verde y fondo verde

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.config(padx=20, pady=20)
ventana.resizable(False, False)  # Deshabilita el redimensionamiento

# Campo de longitud de la contraseña
tk.Label(ventana, text="Longitud de la contraseña:").grid(row=0, column=0, columnspan=2, sticky="w")
entry_longitud = tk.Entry(ventana, width=7)  # Reducir ancho del campo
entry_longitud.grid(row=0, column=1, padx=6, pady=5, sticky="e")  # Alinear a la derecha

# Opciones de configuración
var_mayus = tk.BooleanVar()
boton_mayus = tk.Button(ventana, text="",
                        command=lambda: toggle_opcion(var_mayus, boton_mayus),
                        width=4, relief="raised")
boton_mayus.grid(row=1, column=0, sticky="w")
tk.Label(ventana, text="Incluir Mayúsculas").grid(row=1, column=1, sticky="w")

var_minus = tk.BooleanVar()
boton_minus = tk.Button(ventana, text="",
                        command=lambda: toggle_opcion(var_minus, boton_minus),
                        width=4, relief="raised")
boton_minus.grid(row=2, column=0, sticky="w")
tk.Label(ventana, text="Incluir Minúsculas").grid(row=2, column=1, sticky="w")

var_numeros = tk.BooleanVar()
boton_numeros = tk.Button(ventana, text="",
                        command=lambda: toggle_opcion(var_numeros, boton_numeros),
                        width=4, relief="raised")
boton_numeros.grid(row=3, column=0, sticky="w")
tk.Label(ventana, text="Incluir Números").grid(row=3, column=1, sticky="w")

var_especial = tk.BooleanVar()
boton_especial = tk.Button(ventana, text="",
                        command=lambda: toggle_opcion(var_especial, boton_especial),
                        width=4, relief="raised")
boton_especial.grid(row=4, column=0, sticky="w")
tk.Label(ventana, text="Incluir Caracteres Especiales").grid(row=4, column=1, sticky="w")

# Botón para generar contraseña
boton_generar = tk.Button(ventana, text="Generar Contraseña", command=generar_contraseña)
boton_generar.grid(row=5, column=0, columnspan=2, pady=10)

# Campo para mostrar la contraseña generada, centrado en la ventana
entry_contraseña = tk.Entry(ventana, width=30, justify='center')
entry_contraseña.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Icono del portapapeles para el botón "Copiar" con aspecto de botón
try:
    imagen_portapapeles = Image.open("pass_gen/clipboard_icon.png")
    imagen_portapapeles = imagen_portapapeles.resize((20, 20))  # Redimensionar
    icono_portapapeles = ImageTk.PhotoImage(imagen_portapapeles)
    boton_copiar = tk.Button(ventana, image=icono_portapapeles, command=copiar_contraseña, relief="raised", borderwidth=2)
except FileNotFoundError:
    boton_copiar = tk.Button(ventana, text="Copiar", command=copiar_contraseña, relief="raised", borderwidth=2)

boton_copiar.grid(row=6, column=2, padx=(5, 0), pady=5, sticky="w")

# Etiqueta de confirmación de copia
label_copiado = tk.Label(ventana, text="", fg="green")
label_copiado.grid(row=7, column=0, columnspan=3)

# Menú contextual para copiar contraseña
menu_contextual = tk.Menu(ventana, tearoff=0)
menu_contextual.add_command(label="Copiar", command=copiar_contraseña)

# Asociar el menú contextual al campo de contraseña
entry_contraseña.bind("<Button-3>", mostrar_menu_contextual)  # Clic derecho

ventana.mainloop()
