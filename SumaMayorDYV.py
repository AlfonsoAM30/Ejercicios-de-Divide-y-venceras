def sumaMaxCentral(array, ini, mitad, fin):
    suma = 0
    sumaMaxD = 0
    for i in range(mitad, ini-1, -1):
        suma = suma + array[i]
        if suma > sumaMaxD:
            sumaMaxD = suma
    suma = 0
    sumaMaxI = 0
    for i in range(mitad+1, fin, 1):
        suma = suma + array[i]
        if suma > sumaMaxI:
            sumaMaxI = suma
    return sumaMaxD + sumaMaxI


def sumaMayorProfe(array, ini, fin):
    if ini > fin:
        result = 0
    else:
        if ini == fin:
            result = array[ini]
        else:
            mitad = (ini+fin)//2
            sumaMaxIzq = sumaMayorProfe(array, ini, mitad)
            sumaMaxDer = sumaMayorProfe(array, mitad+1, fin)
            sumaMaxCen = sumaMaxCentral(array, ini, mitad, fin)
            result = max(sumaMaxIzq, sumaMaxDer, sumaMaxCen)
    return result


array = [-2, 11, -4, 13, -5, -2]
ini = 0
fin = len(array)-1
print(sumaMayorProfe(array, ini, fin))