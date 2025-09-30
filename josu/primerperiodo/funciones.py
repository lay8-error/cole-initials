#def nombre_de_la_funcion(parametro1, parametro2):
    #codigo de la funcion

def saludar(nombre):
    mensaje=f"hola, {nombre}"
    print(mensaje)
saludar("Juan")


def sumar(a,b):
    return a+b

def suma():
    n1=int(input("ingrese un número"))
    n2=int(input("ingrese un número"))
    print(n1+n2)

n1=int(input("ingrese un número"))
n2=int(input("ingrese un número"))
resultado=sumar(n1,n2)
print("El resultado es:", resultado)

