nombre=input("ingrese su nombre")
tarea="correr una maratón"
estado="en entrenamiento"

print(f"{nombre} revisando la tarea {tarea}")

if estado=="en entrenamiento":
 print(f"{nombre}, usted sigue {estado}, no pare y siga entrenando")
else:
 print(f"Ha completado su entrenamiento {nombre}, ya puede {tarea}")