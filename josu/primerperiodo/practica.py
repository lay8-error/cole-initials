nombre_completo="Ingrese su nombre completo"
edad_usuario=21
saldo_cuenta=3.99
print(nombre_completo,edad_usuario,saldo_cuenta)

num1=5
num2=10
num3=num1+num2
print(num3)

parte1="Esta es la parte 1"
parte2="Y esta es la parte 2"
frase_completa=parte1+parte2
print(frase_completa)

es_dia_soleado=False
if es_dia_soleado:
 print("Hoy es un dia soleado")
else:
 print("Hoy es un dia nublado")


Lista1=["Manzana","pera","aguacate","aceite de carro","Aceite de moto"]
print("Artículo 2:",Lista1[2])

Lista1[1]="café"
Lista1.append("Empanadas")
Lista1[5]="Empanadas"
print("Lista Modificada:",Lista1)

dict={"título":"Don Quijote de la Mancha","autor":"Miguel de Cervantes","Año de publicación":"1605 d.C"}
print("El autor es",dict["autor"])


edad_str=input("Ingrese su edad")
altura_str=input("Ingrese su altura en metros")
edad_int=int(edad_str)
altura_float=float(altura_str)
print("Tu edad es:", edad_int, "y su tipo es:", type(edad_int))
print("Su altura es",altura_float,"Y su tipo es",type(altura_float))

dias_semana=("lunes","martes","miércoles","jueves","viernes")
print("Primer dia:",dias_semana[0])
print("Ultimo dia",dias_semana[-1])


numeros_con_duplicados = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print("Lista con duplicados:", numeros_con_duplicados)
conjunto_sin_duplicados = set(numeros_con_duplicados)
print("Conjunto sin duplicados:", conjunto_sin_duplicados)
lista_sin_duplicados = list(conjunto_sin_duplicados)
print("Lista resultante sin duplicados:", lista_sin_duplicados)


