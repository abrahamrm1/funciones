def mostrar_perimetro(lado):
    per = lado * 4
    print("El perímetro es:", per)

def mostrar_superficie(lado):
    sup = lado * lado
    print("La superficie es:", sup)

def cargar_dato():
    lado = int(input("Ingrese el valor del lado de un cuadrado: "))
    respuesta = input("¿Quiere calcular el perímetro o la superficie? [ingresar texto: perímetro/superficie]: ")
    
    if respuesta.lower() == "perimetro":
        mostrar_perimetro(lado)
    elif respuesta.lower() == "superficie":
        mostrar_superficie(lado)
    else:
        print("Opción no válida. Por favor, ingrese 'perimetro' o 'superficie'.")

# Programa principal
cargar_dato()
