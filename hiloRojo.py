def busquedaBinaria(data, search, start, end):
    if start > end:
        return -1
    else:
        mitad = (start + end) // 2
        if search == data[mitad]:
            return mitad
        else:
            if search > data[mitad]:
                return busquedaBinaria(data, search, mitad + 1, end)
            else:
                return busquedaBinaria(data, search, start, mitad - 1)


n = int(input().strip())
data1 = list(map(int, input().strip().split()))
m = int(input().strip())
data2 = list(map(int, input().strip().split()))
k = int(input().strip())
for _ in range(k):
    q1, q2 = map(int, input().strip().split())
    p1 = busquedaBinaria(data1, q1, 0, n-1)
    p2 = busquedaBinaria(data2, q2, 0, m-1)
    if p1 >= 0 and p2 >= 0:
        print(str(p1) + " " + str(p2))
    else:
        print("SIN DESTINO")