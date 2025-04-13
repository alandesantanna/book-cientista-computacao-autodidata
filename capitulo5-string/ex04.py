import string

def cifra(astring, chave):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    encrypt = ''

    for c in astring:
        if c in uppercase:
            new = (uppercase.index(c) + chave) % 26 
            encrypt += uppercase[new]
        elif c in lowercase:
            new = (lowercase.index(c) + chave) % 26
            encrypt += lowercase[new]
        else:
            encrypt += c
    return encrypt

# Testando a função
texto = "este é o algoritmo de cifra de César"
chave = 3
texto_cifrado = cifra(texto, chave)
print(f"Texto original: {texto}")
print(f"Texto cifrado: {texto_cifrado}")