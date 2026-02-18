import tkinter as tk
from tkinter import messagebox
import random


def actualizar_clima():
    # Simulamos la lectura de un sensor con un número aleatorio
    temp = random.randint(10, 40)
    label_temp.config(text=f"{temp}°C")

    # Lógica de colores y consejos (Aquí está el aprendizaje)
    if temp < 18:
        color = "#3498db"  # Azul frío
        consejo = "Hace frío. ¡Abrígate!"
    elif 18 <= temp <= 28:
        color = "#2ecc71"  # Verde agradable
        consejo = "El clima está perfecto."
    else:
        color = "#e67e22"  # Naranja calor
        consejo = "Hace mucho calor. Hidrátate."

    ventana.configure(bg=color)
    label_consejo.config(text=consejo, bg=color)
    label_temp.config(bg=color)


# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Deyner Weather Station")
ventana.geometry("400x300")
ventana.configure(bg="#2c3e50")

# Elementos visuales (Widgets)
label_titulo = tk.Label(ventana, text="Temperatura Actual", font=(
    "Arial", 16, "bold"), fg="white", bg="#2c3e50")
label_titulo.pack(pady=20)

label_temp = tk.Label(ventana, text="--°C", font=("Arial",
                      50, "bold"), fg="white", bg="#2c3e50")
label_temp.pack(pady=10)

label_consejo = tk.Label(ventana, text="Presiona el botón para medir", font=(
    "Arial", 12), fg="white", bg="#2c3e50")
label_consejo.pack(pady=10)

# Botón con estilo
btn_medir = tk.Button(ventana, text="ACTUALIZAR SENSOR", font=("Arial", 10, "bold"),
                      command=actualizar_clima, bg="white", fg="black")
btn_medir.pack(pady=20)

ventana.mainloop()
