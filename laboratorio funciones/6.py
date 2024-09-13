def titulo_subrayado(titulo, caracter="*"):
    # Imprimir el título
    print(titulo)
    # Imprimir el carácter subrayado con la misma longitud que el título
    print(caracter * len(titulo))

# Bloque principal
titulo_subrayado("Sistema de Administración")  # Usará '*' como carácter por defecto
titulo_subrayado("Ventas", "-")  # Usará '-' como carácter de subrayado
