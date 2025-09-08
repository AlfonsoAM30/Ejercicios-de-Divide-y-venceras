def binary_search(arr, ini, fin, buscando):
    if ini > fin:
        return -ini
    else:
        medio = (ini + fin)//2
        if buscando == arr[medio]:
            if medio-1 < 0:
                return 0, arr[medio+1]
            elif medio+1 > len(arr)-1:
                return arr[medio-1], 0
            else:
                return arr[medio-1], arr[medio+1]
        elif buscando < arr[medio]:
            return binary_search(arr, ini, medio -1,buscando)
        elif buscando > arr[medio]:
            return binary_search(arr, medio +1, fin, buscando)

universos = list(input().strip().split())
universos.sort()
num = int(input())
for i in range(num):
    a = input()
    sol1, sol2 = binary_search(universos, 0, len(universos)-1, a)
    if sol1 == 0:
        print(f"VACIO {sol2}")
    elif sol2 == 0:
        print(f"{sol1} VACIO")
    else:
        print(f"{sol1} {sol2}")

