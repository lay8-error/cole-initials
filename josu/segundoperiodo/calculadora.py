def suma(a,b):
    resultado=a+b
    return resultado

def resta(a,b):
    resultado=a-b
    return resultado

def división(a,b):
    resultado=a/b
    return resultado

def multiplicacion(a,b):
    resultado=a*b
    return resultado

print(f"1 para sumar, 2 para restar, 3 para dividir, 4 para multiplicar o cualquier otro para salir")
ans=int(input("Ingrese que desea hacer: "))

if ans==1:
    n1=int(input("Ingrese primer número: "))
    n2=int(input("Ingrese segundo número: "))
    resultado=suma(n1,n2)
    print("El resultado de la operación es ", resultado)
elif ans==2:
    n1=int(input("Ingrese primer número: "))
    n2=int(input("Ingrese segundo número: "))
    resultado=resta(n1,n2)
    print("El resultado de la operación es ", resultado)
elif ans==3:
    n1=int(input("Ingrese primer número: "))
    n2=int(input("Ingrese segundo número: "))
    resultado=división(n1,n2)
elif ans==4:
    n1=int(input("Ingrese primer número: "))
    n2=int(input("Ingrese segundo número: "))
    resultado=multiplicacion(n1,n2)
    print("El resultado de la operación es", resultado)
else:
    print("Acción finalizada")

