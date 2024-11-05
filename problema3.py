def ordenar_insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:  # Para orden ascendente
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave

numeros= [12,21,32,6,13,26,3,9,22,18,25,11,7,33,24]
numeros_insercion = numeros[:]
ordenar_insercion(numeros_insercion)
print(f"Orden por inserción: {numeros_insercion}")
