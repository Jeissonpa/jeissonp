"""
#ordenar de manera ascendente
lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
n = len(lista)
iteraciones = 0

for i in range(n):
    for j in range(0, n-i-1):
        iteraciones += 1
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print("Lista ordenada:", lista)
print("Número de iteraciones:", iteraciones)
"""
#ordenar de manera descendente
lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 11]
n = len(lista)
iteraciones = 0

for i in range(n):
    for j in range(0, n-i-1):
        iteraciones += 1
        if lista[j] < lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print("Lista ordenada:", lista)
print("Número de iteraciones:", iteraciones)
