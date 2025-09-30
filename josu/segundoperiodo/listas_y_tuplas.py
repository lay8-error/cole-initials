Lista=[1,2,3,4,5,6,7,8,9,10]
porcion1=Lista[:6]
print(porcion1)
porcion2= Lista[7:]
print(porcion2)
porcion3=Lista[2:8]
print(porcion3)
porcion4=Lista[-5:-1]
print(porcion4)
porcion5=Lista[:]
print(porcion5)
porcion6=Lista[::2]
print(porcion6)

# Definir una lista
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Obtener una porción desde el inicio hasta el índice 6 (sin incluir)
porcion1 = mi_lista[:6]
print(porcion1)  # Imprime [1, 2, 3, 4, 5, 6]

# Obtener una porción desde el índice 7 hasta el final
porcion2 = mi_lista[7:]
print(porcion2)  # Imprime [8, 9, 10]

# Obtener una porción desde el índice 2 hasta el índice 8 (sin incluir)
porcion3 = mi_lista[2:8]
print(porcion3)  # Imprime [3, 4, 5, 6, 7, 8]

# Utilizar índices negativos para contar desde el final
porcion4 = mi_lista[-5:-1]
print(porcion4)  # Imprime [6, 7, 8, 9]

# Obtener toda la lista (equivalente a lista[:])
copia_completa = mi_lista[:]
print(copia_completa)  # Imprime [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Obtener una porción con un paso (cada segundo elemento)
porcion_con_paso = mi_lista[::2]
print(porcion_con_paso)  # Imprime [1, 3, 5, 7, 9]


lista_numeros=[1,2,3,4,5]
lista_strings=["Piña","manzana","pera","clavito"]
lista_mixta=[10,"tigre",True,3.99]

primer_elemento = lista_numeros[0]
segundo_elemento = lista_strings[1]
ultimo_elemento = lista_mixta[-1]
#cuenta los caractéres de la lista
long = len(lista_mixta)
print(long)

#agrega cosas al final de la lista
lista_numeros.append(6)

#Agrega cosas en un lugar determinado de la lista
lista_strings.insert(1, "orange")

#elimina el último elemento de la lista
ultimo_elemento = lista_numeros.pop()

#elimina algo específico de la lista
lista_strings.remove("banana")

#ordena la lista
lista_numeros.sort()

#invierte la lista
lista_mixta.reverse() 