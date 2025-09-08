import sys
def binary_search(arr, ini, fin, buscando, trys):
    if ini > fin:
        return -ini
    else:
        medio = (ini + fin)//2
        if buscando == arr[medio]:
            return trys, medio
        elif buscando < arr[medio]:
            return binary_search(arr, ini, medio -1,buscando, trys+1)
        elif buscando > arr[medio]:
            return binary_search(arr, medio +1, fin, buscando, trys+1)

n, m, p = map(int, input().strip().split())

habitaciones = list(map(int, input().strip().split()))

sol, medio = binary_search(habitaciones,0, n-1, p, 1)

if (sol <= m):
    print(f"Penny esta en la habitacion {medio}, se han requerido {sol} saltos")
else:
    sys.stdout.buffer.write("¿Donde esta Penny?".encode('utf-8'))