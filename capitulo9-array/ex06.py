def separar_pares_impares(an_array):
    
    pares = []
    impares = []
    
    for numero in an_array:
        if numero % 2 == 0:
            pares.append(numero)  # Adiciona aos pares
        else:
            impares.append(numero)  # Adiciona aos ímpares
    
    resultado = []
    
    for par in pares:
        resultado.append(par)
    
    for impar in impares:
        resultado.append(impar)
    
    return resultado



an_array = [1, 2, 3, 4, 5, 6, 7, 8]
resultado = separar_pares_impares(an_array)
print("Resultado:", resultado)