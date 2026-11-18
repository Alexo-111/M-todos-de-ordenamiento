def insercion(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]   # desplaza elementos a la derecha
            j -= 1
        lista[j + 1] = actual         # inserta en su lugar
    return lista


nombres = ["Carlos", "Ana", "Luis", "Beatriz", "Daniel"]
print("Nombres originales:", nombres)
print("Nombres ordenados: ", insercion(nombres))