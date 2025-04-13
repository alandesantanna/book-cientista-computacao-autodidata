def bubble_sort(lista):
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(tamanho - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp

numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", numeros)

bubble_sort(numeros)

print("Lista ordenada:", numeros)