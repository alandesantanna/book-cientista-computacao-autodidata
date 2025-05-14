class FilaComDuasPilhas:
    def __init__(self):
        self.pilha1 = []
        self.pilha2 = []

    def enqueue(self, item):
        self.pilha1.append(item)

    def dequeue(self):
        if not self.pilha2:
            while self.pilha1:
                self.pilha2.append(self.pilha1.pop())
        if not self.pilha2:
            raise IndexError("A fila está vazia")
        return self.pilha2.pop()


fila = FilaComDuasPilhas()
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)

print(fila.dequeue())
print(fila.dequeue())
fila.enqueue(4)
print(fila.dequeue())
print(fila.dequeue())