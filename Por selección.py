def seleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        indice_min = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_min]:
                indice_min = j
        lista[i], lista[indice_min] = lista[indice_min], lista[i]
    return lista


precios = [150.50, 20.00, 99.99, 45.75, 10.25]
print("Precios originales:", precios)
print("Precios ordenados: ", seleccion(precios))