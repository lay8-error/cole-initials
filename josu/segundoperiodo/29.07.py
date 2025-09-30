frutas=["manzana","banana","cereza","dátil"]
print(frutas)
print(frutas[0])
print(frutas[3])
print(frutas[2])
colores = ["rojo", "verde", "azul"]
print(colores)
colores[1]="amarillo"
print(colores)
colores.append("morado")
print(colores)
colores[1:1]=["naranja"]
print(colores)
numeros = [10, 5, 20, 15, 25]
numeros.append(30)
print(numeros)
numeros.remove(5)
print(numeros)
elemento_final=numeros.pop()
print(numeros)
print(elemento_final)
numeros.sort()
print(numeros)
ciudades=["Tokyo","Nagazaki","Kawasaki","Osaka"]
print(len(ciudades))
resultado="Londres" in ciudades
print(resultado)
resultado="Tokyo"in ciudades
print(resultado)
mixta=[5,3.99,"Ary",True]
print(mixta)
for elementos in mixta:
    print(type(elementos))   