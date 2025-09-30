def area_rectangulo(base,altura):
    area= base*altura
    return area

base=int(input("Ingrese la base del rectángulo"))
altura=int(input("Ingrese la altura del triángulo"))

area=area_rectangulo(base,altura)
print(area)

print(dir(__builtins__))
help(print)