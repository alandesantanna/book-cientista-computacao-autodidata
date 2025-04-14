palavras = ["algoritmo", "código", "Python", "dados", "função", "laço", "variável", "teste", "cifra", "computação"]

palavras_filtradas = [palavra for palavra in palavras if len(palavra) > 4]

print(f"Palavras originais: {palavras}")
print(f"Palavras com mais de 4 caracteres: {palavras_filtradas}")