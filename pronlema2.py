def ordenar_burbuja(lista): 
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:  # Para orden ascendente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Lista de nombres
nombres = ["Guadalupe", "Vladimir", "José", "Juan", "Mateo", "Miguel", 
           "Sebastián", "Rodrigo", "Emir", "Rogelio", "Sergio", "Alan", 
           "María", "Issac", "Rafael", "Ximena", "Ashlee", "Norberto", 
           "Nayency", "Pablo", "Odalys", "Omar", "Damián", "Diego", 
           "Carime", "Karla", "Josef", "Víctor", "Reyna", "Ana"]

# Ordenamientos
nombres_burbuja = nombres[:]
ordenar_burbuja(nombres_burbuja)
print(f"Orden por burbuja: {nombres_burbuja}")


