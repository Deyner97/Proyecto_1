import tkinter as tk
from tkinter import messagebox

# --- FUNCIONES DE LÓGICA ---


def click_boton(valor):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, str(actual) + str(valor))


def borrar():
    entrada.delete(0, tk.END)


def calcular(event=None):  # Añadimos event=None para que funcione con Enter
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception:
        messagebox.showerror("Error", "Operación no válida")

# --- FUNCIÓN PARA EL TECLADO ---


def manejar_teclado(event):
    tecla = event.char
    # Si es un número o un operador válido
    if tecla in "0123456789+-*/.":
        click_boton(tecla)
    # Si presionas Enter (Return)
    elif event.keysym == "Return":
        calcular()
    # Si presionas Escape, limpia la pantalla
    elif event.keysym == "Escape":
        borrar()
    # Si presionas BackSpace, borra el último carácter
    elif event.keysym == "BackSpace":
        actual = entrada.get()
        entrada.delete(0, tk.END)
        entrada.insert(0, actual[:-1])

# --- FUNCIONES HOVER (Se mantienen igual) ---


def al_entrar(e):
    e.widget.original_color = e.widget.cget("background")
    e.widget.config(background="#5D6D7E")


def al_salir(e):
    e.widget.config(background=e.widget.original_color)


# --- CONFIGURACIÓN DE LA VENTANA ---
ventana = tk.Tk()
ventana.title("Calculadora Pro de Deyner")
ventana.geometry("300x400")
ventana.configure(bg="#2c3e50")

# Vinculamos el teclado a TODA la ventana
ventana.bind("<Key>", manejar_teclado)

# Pantalla de entrada (Deshabilitamos escritura directa para evitar errores)
entrada = tk.Entry(ventana, font=("Arial", 24),
                   borderwidth=5, relief="flat", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

botones = ['7', '8', '9', '/', '4', '5', '6',
           '*', '1', '2', '3', '-', 'C', '0', '=', '+']

fila = 1
columna = 0

for boton in botones:
    if boton == "=":
        color_bg = "#27ae60"
    elif boton == "C":
        color_bg = "#e74c3c"
    else:
        color_bg = "#34495e"

    btn = tk.Button(ventana, text=boton, bg=color_bg,
                    fg="white", font=("Arial", 14))

    # Configuramos comandos de los botones del mouse
    if boton == "C":
        btn.config(command=borrar)
    elif boton == "=":
        btn.config(command=calcular)
    else:
        btn.config(command=lambda b=boton: click_boton(b))

    btn.grid(row=fila, column=columna, padx=2, pady=2, sticky="nsew")
    btn.bind("<Enter>", al_entrar)
    btn.bind("<Leave>", al_salir)

    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)
for i in range(1, 5):
    ventana.grid_rowconfigure(i, weight=1)

ventana.mainloop()
