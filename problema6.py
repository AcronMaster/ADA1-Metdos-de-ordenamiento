def ordenar_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_indx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_indx]:  # Para orden ascendente
                min_indx = j
        lista[i], lista[min_indx] = lista[min_indx], lista[i]

nombres= ["plátano", "manzana", "pera", "uva", "melon", "sandia", "kiwi", "mango", "limon", "papaya", "coco", "jicama", "zanahoria", "melocoton", "cereza", "fresa", "piña", "naranja", "guayaba"]
nombres_seleccion = nombres[:]
ordenar_seleccion(nombres_seleccion)
print(f"Orden por selección: {nombres_seleccion}")