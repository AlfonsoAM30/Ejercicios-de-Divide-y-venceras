def elevar(numero, potencia):
    sol = 1
    if potencia == 0:
        sol = 1
    else:
        if potencia == 1:
            sol = numero
        else:
            if(potencia % 2 == 0):
                pot = elevar(numero, potencia//2)
                sol = pot * pot
            elif(potencia % 2 != 0):
                sol = numero * elevar(numero, potencia-1)
    return sol


numero, potencia = map(int, input().strip().split())
print(elevar(numero, potencia))