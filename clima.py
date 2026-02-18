import tkinter as tk
import random


def actualizar_clima():
    # Simulamos la temperatura
    temp = random.randint(10, 40)
    label_temp.config(text=f"{temp}°C")

    # Lógica de colores, consejos e ICONOS
    if temp < 18:
        color = "#3498db"  # Azul
        consejo = "Hace frío. ¡Abrígate!"
        icono = "❄️"      # Icono de nieve
    elif 18 <= temp <= 28:
        color = "#2ecc71"  # Verde
        consejo = "El clima está perfecto."
        icono = "☀️"      # Icono de sol despejado
    else:
        color = "#e67e22"  # Naranja
        consejo = "Hace mucho calor. Hidrátate."
        icono = "🔥"      # Icono de fuego/calor extremo

    # Aplicar cambios visuales
    ventana.configure(bg=color)
    label_titulo.config(bg=color)
    label_temp.config(bg=color)
    label_consejo.config(text=consejo, bg=color)
    label_icono.config(text=icono, bg=color)


# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Estación Climática de Deyner")
ventana.geometry("400x450")
ventana.configure(bg="#2c3e50")

# --- ELEMENTOS VISUALES ---

label_titulo = tk.Label(ventana, text="ESTADO DEL TIEMPO", font=(
    "Arial", 14, "bold"), fg="white", bg="#2c3e50")
label_titulo.pack(pady=20)

# Este es el nuevo label para el icono
label_icono = tk.Label(ventana, text="☁️", font=("Arial", 80), bg="#2c3e50")
label_icono.pack(pady=10)

label_temp = tk.Label(ventana, text="--°C", font=("Arial",
                      45, "bold"), fg="white", bg="#2c3e50")
label_temp.pack(pady=5)

label_consejo = tk.Label(ventana, text="Pulsa el botón para sensorizar", font=(
    "Arial", 12, "italic"), fg="white", bg="#2c3e50")
label_consejo.pack(pady=15)

# Botón de acción
btn_medir = tk.Button(ventana, text="ACTUALIZAR DATOS", font=("Arial", 10, "bold"),
                      command=actualizar_clima, bg="white", fg="#2c3e50", padx=10, pady=5)
btn_medir.pack(pady=20)

ventana.mainloop()
