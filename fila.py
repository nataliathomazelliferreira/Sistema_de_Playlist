class NodoFila:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def enfileirar(self, musica):
        novo = NodoFila(musica)

        if self.esta_vazia():
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

        self.tamanho += 1

    def desenfileirar(self):
        if self.esta_vazia():
            return None

        musica = self.inicio.musica
        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        self.tamanho -= 1
        return musica

    def listar(self):
        if self.esta_vazia():
            print("Fila vazia.")
            return

        atual = self.inicio

        while atual is not None:
            atual.musica.exibir()
            print("-" * 30)
            atual = atual.proximo