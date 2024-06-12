import tkinter as tk
from tkinter import messagebox

def calcular_factorial():
    try:
        numero = int(entry_numero.get())
        resultado = factorial(numero)
        messagebox.showinfo("Resultado", f"El factorial de {numero}! es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número entero válido.")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Factorial")

# Crear etiqueta y campo de entrada
label_numero = tk.Label(root, text="Ingresa un número:")
label_numero.pack()
entry_numero = tk.Entry(root)
entry_numero.pack()

# Crear botón de calcular
button_calcular = tk.Button(root, text="Calcular Factorial", command=calcular_factorial)
button_calcular.pack()

# Ejecutar el bucle principal de la aplicación
root.mainloop()
