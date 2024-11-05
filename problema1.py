def ordenar_burbuja(lista): 
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] < lista[j + 1]:  # Para orden descendente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
# Lista original
numeros = [130, 345, 280, 300, 420, 100, 510, 240, 370, 360, 150, 560]

# Ordenamientos
numeros_burbuja = numeros[:]
ordenar_burbuja(numeros_burbuja)
print(f"Orden por burbuja: {numeros_burbuja}")
