from musica import Musica
from lista import NodoLista

class Biblioteca:
    def __init__(self):
        self.inicio = None
        self.proximo_id = 1
        self.total = 0

    def adicionar(self, titulo, artista, genero, bpm):
        musica = Musica(self.proximo_id, titulo, artista, genero, bpm)
        novo = NodoLista(musica)

        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio

            while atual.proximo is not None:
                atual = atual.proximo

            atual.proximo = novo

        self.proximo_id += 1
        self.total += 1
        print("Música adicionada com sucesso.")

    def remover(self, id):
        if self.inicio is None:
            print("Biblioteca vazia.")
            return

        if self.inicio.musica.id == id:
            self.inicio = self.inicio.proximo
            self.total -= 1
            print("Música removida com sucesso.")
            return

        anterior = self.inicio
        atual = self.inicio.proximo

        while atual is not None:
            if atual.musica.id == id:
                anterior.proximo = atual.proximo
                self.total -= 1
                print("Música removida com sucesso.")
                return

            anterior = atual
            atual = atual.proximo

        print("ID inexistente.")

    def buscar_por_id(self, id):
        atual = self.inicio

        while atual is not None:
            if atual.musica.id == id:
                return atual.musica

            atual = atual.proximo

        return None

    def buscar_por_titulo(self, titulo):
        atual = self.inicio

        while atual is not None:
            if atual.musica.titulo.lower() == titulo.lower():
                return atual.musica

            atual = atual.proximo

        return None

    def listar(self):
        if self.inicio is None:
            print("Biblioteca vazia.")
            return

        atual = self.inicio

        while atual is not None:
            atual.musica.exibir()
            print("-" * 30)
            atual = atual.proximo