import math

def area_circulo(radio):
    area=math.pi*radio*radio
    print(area)

ans=int(input("Ingrese el área del círculo: "))
area_circulo(ans)
