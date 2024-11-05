def ordenar_insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:  # Para orden ascendente
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave

nombres= ["Jose", "Maria", "Mario", "Jacinto", "Pablo", "Adrian", "Luis", "Carmen", "Zobeyda", "Benjamin", "Diego", "Edgar", "Marcos", "Yazmari", "Saul", "Efraín", "Fernanda", "Karolina"]
nombres_insercion = nombres[:]
ordenar_insercion(nombres_insercion)
print(f"Orden por inserción: {nombres_insercion}")