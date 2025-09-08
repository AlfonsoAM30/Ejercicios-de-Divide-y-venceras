def binary_search(arr, ini, fin, buscando):
    if ini > fin:
        return -ini
    else:
        medio = (ini + fin)//2
        if buscando == arr[medio]:
            return medio
        elif buscando < arr[medio]:
            return binary_search(arr, ini, medio -1, buscando)
        elif buscando > arr[medio]:
            return binary_search(arr, medio +1, fin, buscando)

if __name__ == '__main__':
    arr = [1, 3, 5, 7, 8, 10, 12, 15]
    ini = 0
    fin = len(arr) - 1

    buscando = 10
    posicion = binary_search(arr, ini, fin, buscando)

    if posicion >= 0:
        print("El elemento",buscando,"esta en la posicion", posicion)
    else:
        print("Elemento",buscando,"no esta en el array")
