def build_family_tree(data):
    tree = {} #creamos el diccionario
    for line in data: #para cada elemento en data, en los cuales cada line es una tupla
        parent = line[0] #el primer elemento es nuestro identificador
        children = line[1:] #ftodo lo demas son los hijos del identificador
        tree[parent] = children #hacemos que el label/key sea el padre y los demas seran la tupla de los hijos
    return tree #devolvemos el diccionario


def find_root(tree):
    all_members = set(tree.keys()) #hacemos que todos los miembros sean una lista con set() para que no se repitan
    all_children = {child for children in tree.values() for child in children} #por cada hijo lo metemos en la lista
    return list(all_members - all_children)[0] #devolvemos la lista con los padres que nos son hijos de nadie


def calculate_level(member, tree, levels, current_level=1):
    if member not in levels:  # para evitar ciclos
        levels[member] = current_level #para cada miembro de la familia se le va poniendo su nivel
        for child in tree.get(member, []): #haciedno tree.get(member, []) nos devueleve una lista con los hijos de ese miembro e iteramos el for por cada hijo
            calculate_level(child, tree, levels, current_level + 1) #llamamos recursivamente para cada hijo


def solve_family_query(data, queries):
    family_tree = build_family_tree(data) #Nos creamos un diccionario donde la level es nuestro identificador de cada persona
    root = find_root(family_tree) #nos devuelve la persona inicial, el primer elemento

    levels = {} #creamos un diccionario vacio para los niveles
    calculate_level(root, family_tree, levels) #nos devuelve un diccionario para con cada miembro y su nivel correspondiente

    return [levels[query] for query in queries] #devolvemos la lista con los niveles de los miembros de los que queremos saber el nivel


n = int(input())
data = []
for _ in range(n):
    family = tuple(map(int, input().split())) #family es nuestra tupla que acabamos de ingresar por terminal
    data.append(family) #Es una lista de tuplas

m = int(input())
queries = []
for _ in range(m):
    a = int(input()) #Son los hijos de los que queremos saber el nivel
    queries.append(a) #lista de los hijos

results = solve_family_query(data, queries) #con los datos de las tuplas y de los que queremos saber el nivel
for result in results:
    print(result)
