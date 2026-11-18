def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        intercambio = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        if not intercambio:      # si no hubo cambios, ya está ordenada
            break
    return lista


calificaciones = [8.5, 6.0, 9.5, 7.2, 10.0, 5.8]
print("Calificaciones originales:", calificaciones)
print("Calificaciones ordenadas: ", burbuja(calificaciones))