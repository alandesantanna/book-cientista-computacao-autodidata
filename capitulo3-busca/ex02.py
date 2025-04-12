palavras = [
    "abacate", "abacaxi", "abelha", "abóbora", "abrigo", "absurdo", "academia", "acidente", "acompanhar", "acorde",
    "admirar", "adolescente", "adulto", "aeroporto", "afeto", "água", "alegria", "alface", "algodão", "alimento",
    "almofada", "amarelo", "amigo", "amor", "análise", "anel", "animal", "aniversário", "anjo", "antena",
    "antigo", "aparelho", "apetite", "aprender", "apresentar", "árvore", "asa", "atitude", "atleta", "atual",
    "aula", "aumento", "aventura", "avião", "avó", "azul", "bala", "banana", "bandeira", "barco",
    "barriga", "bateria", "beleza", "belo", "bicicleta", "biscoito", "blusa", "bola", "bolsa", "bombeiro",
    "borboleta", "branco", "brilho", "brincadeira", "brinquedo", "broa", "cabeça", "caderno", "café", "caixa",
    "calendário", "calor", "cama", "caminho", "camisa", "campo", "caneta", "canguru", "cantar", "capricho",
    "carinho", "carro", "carta", "casa", "casaco", "cavalo", "cebola", "celular", "cenoura", "cereja",
    "certeza", "chapéu", "chuva", "cidadão", "cidade", "cinto", "circo", "clima", "coração", "coragem"
]

def busca_binaria(lista, palavra):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == palavra:
            return meio
        elif lista[meio] < palavra:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

# Testando a busca binária
palavra_procurada = "coração"
indice = busca_binaria(palavras, palavra_procurada)

if indice != -1:
    print(f"A palavra '{palavra_procurada}' foi encontrada no índice {indice}.")
else:
    print(f"A palavra '{palavra_procurada}' não foi encontrada na lista.")