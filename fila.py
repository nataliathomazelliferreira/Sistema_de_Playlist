class NodoFila:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def enqueue(self, musica):
        novo_nodo = NodoFila(musica)

        if self.inicio is None:
            self.inicio = novo_nodo
            self.fim = novo_nodo
        else:
            self.fim.proximo = novo_nodo
            self.fim = novo_nodo

        self.tamanho += 1

    def dequeue(self):
        if self.inicio is None:
            return None

        musica = self.inicio.musica
        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        self.tamanho -= 1
        return musica

    def limpar(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def exibir(self):
        if self.inicio is None:
            print("Fila vazia.")
            return

        atual = self.inicio

        while atual is not None:
            atual.musica.exibir()
            print("-" * 30)
            atual = atual.proximo