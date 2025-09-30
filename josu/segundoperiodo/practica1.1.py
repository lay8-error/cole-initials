def bienvenida(nombre, idioma="español"):
    if idioma.lower() == "español":
        print(f"Hola {nombre}, bienvenido a mi algoritmo")
    else:
        print(f"Hello {nombre}, welcome to my algorithm")

# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
ans = input("Elija un idioma (Español o Inglés): ").strip().lower()

# Llamar a la función respetando el idioma por defecto
if ans == "inglés":
    bienvenida(nombre, idioma="ingles")
else:
    bienvenida(nombre)  # No se pasa idioma, se usa el valor por defecto
