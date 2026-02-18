import tkinter as tk
from tkinter import messagebox


def click_boton(valor):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, str(actual) + str(valor))


def borrar():
    entrada.delete(0, tk.END)


def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception:
        messagebox.showerror("Error", "Operación no válida")


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Deyner")
ventana.geometry("300x400")
ventana.configure(bg="#2c3e50")

# Pantalla de entrada
entrada = tk.Entry(ventana, font=("Arial", 24),
                   borderwidth=5, relief="flat", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Definición de botones
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

fila = 1
columna = 0

for boton in botones:
    if boton == "=":
        tk.Button(ventana, text=boton, width=5, height=2, bg="#27ae60", fg="white", font=("Arial", 14, "bold"),
                  command=calcular).grid(row=fila, column=columna, padx=2, pady=2, sticky="nsew")
    elif boton == "C":
        tk.Button(ventana, text=boton, width=5, height=2, bg="#e74c3c", fg="white", font=("Arial", 14, "bold"),
                  command=borrar).grid(row=fila, column=columna, padx=2, pady=2, sticky="nsew")
    else:
        tk.Button(ventana, text=boton, width=5, height=2, bg="#34495e", fg="white", font=("Arial", 14),
                  command=lambda b=boton: click_boton(b)).grid(row=fila, column=columna, padx=2, pady=2, sticky="nsew")

    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Hacer que los botones se expandan uniformemente
for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)
for i in range(1, 5):
    ventana.grid_rowconfigure(i, weight=1)

ventana.mainloop()
