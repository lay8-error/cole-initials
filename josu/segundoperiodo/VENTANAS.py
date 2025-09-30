import tkinter as tk
from  tkinter import ttk

def agregar_caracter(caracter):
    pantalla.insert(tk.END,caracter)

def limpiar_pantalla():
    pantalla.delete(0,tk.END)

def calcular_resultado():
    try:
        expresion=pantalla.get()
        resultado=eval(expresion)
        pantalla.delete(0,tk.END)
        pantalla.insert(tk.END, str(resultado))
    except Exception as e:
        pantalla.delete(0,tk.END)
        pantalla.insert(tk.END, "Error")



root=tk.Tk()
root.title("Calculadora")
pantalla=tk.Entry(root, width=25, font=("arial",24))
pantalla.grid(row=0, column=0, columnspan=4)
botoness= ["7","8","9","/",
           "4","5","6","-",
           "7","8","9","+","*"]

fila=1
columna=0
for boton_texto in botoness:

    tk.Button(root, text=boton_texto, width=5, height=2, command=lambda b=boton_texto: agregar_caracter(b)).grid(row=fila, column=columna)

    columna+=1
    if columna>3:
        columna=0
        fila+=1

# Botón de limpiar (C)
tk.Button(root, text='C', width=5, height=2, command=limpiar_pantalla).grid(row=fila, column=0)
tk.Button(root, text="=", width=5, height=2, command=calcular_resultado).grid(row=fila, column=1)
root.mainloop()
# Botón para calcular (se puede asignar a '=')
# El "=" ya está incluido en el bucle, asumiendo que la lógica para '=' está en agregar_caracter
# Para una lógica de "=" distinta, necesitarías otro botón y su comando.





root.mainloop()