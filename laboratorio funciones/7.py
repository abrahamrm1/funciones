def cargar():
    lista = []
    for x in range(10):
        valor = int(input("Ingrese valor: "))
        lista.append(valor)
    return lista

def imprimir(lista):
    # Unir los elementos de la lista en un string separado por comas
    print(",".join(map(str, lista)))

# Bloque principal
lista = cargar()
imprimir(lista)
