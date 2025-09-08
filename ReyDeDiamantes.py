def binary_search(arr, ini, fin, buscando):
    if ini > fin:
        return -ini
    else:
        medio = (ini + fin)//2
        if buscando == arr[medio]:
            arr[medio] = 'X'
            return True
        elif buscando < arr[medio]:
            return binary_search(arr, ini, medio -1, buscando)
        elif buscando > arr[medio]:
            return binary_search(arr, medio +1, fin, buscando)


n = int(input())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
quests = list(map(int, input().strip().split()))
for quest in quests:
    binary_search(grid, 0, len(grid)-1, quest)

