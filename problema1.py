def ordenar_burbuja(lista): 
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] < lista[j + 1]:  # Para orden descendente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def ordenar_inserccion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave > lista[j]:  # Para orden descendente
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave

def ordenar_seleccion(lista):
    n = len(lista)
    for i in range(n):
        max_indx = i
        for j in range(i + 1, n):
            if lista[j] > lista[max_indx]:  # Para orden descendente
                max_indx = j
        lista[i], lista[max_indx] = lista[max_indx], lista[i]

# Lista original
numeros = [130, 345, 280, 300, 420, 100, 510, 240, 370, 360, 150, 560]

# Ordenamientos
numeros_burbuja = numeros[:]
ordenar_burbuja(numeros_burbuja)
print(f"Orden por burbuja: {numeros_burbuja}")

numeros_insercion = numeros[:]
ordenar_inserccion(numeros_insercion)
print(f"Orden por inserción: {numeros_insercion}")

numeros_seleccion = numeros[:]
ordenar_seleccion(numeros_seleccion)
print(f"Orden por selección: {numeros_seleccion}")

