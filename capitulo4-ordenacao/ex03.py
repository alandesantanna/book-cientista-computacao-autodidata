def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x <= pivo]
        maiores = [x for x in lista[1:] if x > pivo]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)

numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", numeros)

numeros_ordenados = quick_sort(numeros)

print("Lista ordenada:", numeros_ordenados)