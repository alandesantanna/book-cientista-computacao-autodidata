class Pilha:
    def __init__(self):
        self.itens = []

    def inserir(self, item):
        self.itens.append(item)

    def remover(self):
        if not self.vazia():
            return self.itens.pop()
        return None

    def tamanho(self):
        return len(self.itens)

    def vazia(self):
        return len(self.itens) == 0

    def topo(self):
        if not self.vazia():
            return self.itens[-1]
        return None


def menu():
    pilha = Pilha()
    while True:
        print("\n1. Inserir")
        print("2. Remover")
        print("3. Ver topo")
        print("4. Ver tamanho")
        print("5. Ver se está vazia")
        print("6. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            item = input("Item: ")
            pilha.inserir(item)
            print(f"'{item}' adicionado.")
        elif opcao == "2":
            item = pilha.remover()
            print(f"'{item}' removido." if item else "Pilha vazia.")
        elif opcao == "3":
            item = pilha.topo()
            print(f"Topo: '{item}'." if item else "Pilha vazia.")
        elif opcao == "4":
            print(f"Tamanho: {pilha.tamanho()}.")
        elif opcao == "5":
            print("Vazia." if pilha.vazia() else "Não está vazia.")
        elif opcao == "6":
            break
        else:
            print("Opção inválida.")

menu()

