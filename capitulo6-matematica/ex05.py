def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Lista de números primos até 1000
numeros_primos = [n for n in range(2, 101) if eh_primo(n)]

print(f"Números primos até 1000: {numeros_primos}")