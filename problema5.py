def ordenar_seleccion(lista):
    n = len(lista)
    for i in range(n):
        max_indx = i
        for j in range(i + 1, n):
            if lista[j] > lista[max_indx]:  # Para orden descendente
                max_indx = j
        lista[i], lista[max_indx] = lista[max_indx], lista[i]

numeros=[59,21,35,46,99,129,110,210,233,301,60,11,87,329,259,219,179,199]

numeros_seleccion = numeros[:]
ordenar_seleccion(numeros_seleccion)
print(f"Orden por selección: {numeros_seleccion}")