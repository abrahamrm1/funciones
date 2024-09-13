def sumar(v1, v2, *lista):
    # Inicializar la suma con los dos primeros valores
    suma = v1 + v2
    # Sumar los valores adicionales en *lista
    for x in lista:
        suma += x
    return suma

# Bloque principal
print("La suma de 1 + 2 es:", sumar(1, 2))
print("La suma de 1 + 2 + 3 + 4 es:", sumar(1, 2, 3, 4))
print("La suma de 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 es:", sumar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
