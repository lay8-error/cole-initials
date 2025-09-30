import tkinter as tk

def agregar_caracter(caracter):
    pantalla.insert(tk.END, caracter)

def limpiar_pantalla():
    pantalla.delete(0, tk.END)

def calcular_resultado():
    try:
        expresion = pantalla.get()
        resultado = eval(expresion)
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(resultado))
    except Exception as e:
        pantalla.delete(0 , tk.END)
        pantalla.insert(tk.END, "ERROR")

def convertir():
    try:
        expresion = int(pantalla.get())
        resultado = int(expresion/499.97)
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(resultado))
    except Exception as e:
        pantalla.delete(0 , tk.END)
        pantalla.insert(tk.END, "ERROR")

def convertir2():
    try:
        expresion = int(pantalla.get())
        resultado = int(expresion*499.97)
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(resultado))
    except Exception as e:
        pantalla.delete(0 , tk.END)
        pantalla.insert(tk.END, "ERROR")

ventana = tk.Tk()
ventana.title("Calculadora")
pantalla = tk.Entry(ventana, width=20, font=("arial", 16) )
pantalla.grid(row=0, column=0, columnspan=4)

botones = [
    "7", "8", "9" , "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", ",", "+"
]

fila = 1
columna = 0

for boton_texto in botones:
    tk.Button(ventana, text=boton_texto, width=5, height=2, command=lambda b=boton_texto: agregar_caracter(b)).grid(row=fila, column=columna)
    columna +=1
    if columna > 3:
        columna = 0
        fila +=1 

tk.Button(ventana, text="C", width=5, height=2, command=limpiar_pantalla).grid(row=fila, column=0)
tk.Button(ventana, text="=", width=5, height=2, command=calcular_resultado).grid(row=fila, column=1)
tk.Button(ventana, text="CONV₡-$", width=8, height=2, command=convertir).grid(row=fila, column=2)
tk.Button(ventana, text="CONV$-₡", width=8, height=2, command=convertir2).grid(row=fila, column=3)
ventana.mainloop()