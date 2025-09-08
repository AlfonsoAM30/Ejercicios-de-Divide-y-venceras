def Merge(parteIzq, parteDer):
    arrSolucion = []
    while len(parteIzq) > 0 and len(parteDer) > 0:
        if parteIzq[0] < parteDer[0]:
            arrSolucion.append(parteIzq[0])
            parteIzq.pop(0)
        else:
            arrSolucion.append(parteDer[0])
            parteDer.pop(0)
    while len(parteIzq) > 0:
        arrSolucion.append(parteIzq[0])
        parteIzq.pop(0)
    while len(parteDer) > 0:
        arrSolucion.append(parteDer[0])
        parteDer.pop(0)
    return arrSolucion


def ordenar(arr):
    if len(arr) <= 1:
        return arr

    medio = len(arr)//2
    izq = arr[:medio]
    der = arr[medio:]
    parteIzq = ordenar(izq)
    parteDer = ordenar(der)
    return Merge(parteIzq, parteDer)


arr = [2, 4, 5, 1, 3]
ordenado = ordenar(arr)
print(ordenado)

