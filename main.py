
from biblioteca import Biblioteca
from fila import Fila

def ler_bpm():
    while True:
        valor = input("BPM: ")

        if valor.isdigit():
            bpm = int(valor)

            if bpm > 0:
                return bpm

            else:
                print("O BPM deve ser maior que zero.")

        else:
            print("Digite um BPM numérico.")

def escolher_fila(filas):
    print("1 - Relaxar")
    print("2 - Focar")
    print("3 - Animar")
    print("4 - Treinar")

    opcao = input("Escolha uma fila: ")

    if opcao == "1":
        return filas["relaxar"]

    if opcao == "2":
        return filas["focar"]

    if opcao == "3":
        return filas["animar"]

    if opcao == "4":
        return filas["treinar"]

    print("Opção inválida.")
    return None

def criar_filas():
    return {
        "relaxar": Fila(),
        "focar": Fila(),
        "animar": Fila(),
        "treinar": Fila()
    }

def montar_filas(biblioteca):
    filas = criar_filas()

    atual = biblioteca.inicio

    while atual is not None:
        musica = atual.musica

        if musica.bpm <= 80:
            filas["relaxar"].enfileirar(musica)

        elif musica.bpm <= 120:
            filas["focar"].enfileirar(musica)

        elif musica.bpm <= 160:
            filas["animar"].enfileirar(musica)

        else:
            filas["treinar"].enfileirar(musica)

        atual = atual.proximo

    print("Filas montadas com sucesso.")
    return filas

def carregar_musicas(biblioteca):
    try:
        arquivo = open("musicas.txt", "r", encoding="utf-8")

        for linha in arquivo:
            linha = linha.strip()

            if linha == "":
                continue

            artista, titulo, genero, bpm = linha.split(";")

            biblioteca.adicionar(
                titulo,
                artista,
                genero,
                int(bpm)
            )

        arquivo.close()

    except FileNotFoundError:
        print("Arquivo de músicas não encontrado.")

def adicionar_musica(biblioteca):
    titulo = input("Título: ")
    artista = input("Artista: ")
    genero = input("Gênero: ")
    bpm = ler_bpm()

    biblioteca.adicionar(titulo, artista, genero, bpm)

def remover_musica(biblioteca):
    try:
        id = int(input("ID da música: "))
        biblioteca.remover(id)

    except ValueError:
        print("Digite um ID numérico.")

def buscar_musica(biblioteca):
    print("1 - Buscar por ID")
    print("2 - Buscar por título")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try:
            id = int(input("ID: "))
            musica = biblioteca.buscar_por_id(id)

        except ValueError:
            print("Digite um ID numérico.")
            return

    elif opcao == "2":
        titulo = input("Título: ")
        musica = biblioteca.buscar_por_titulo(titulo)

    else:
        print("Opção inválida.")
        return

    if musica is None:
        print("Música não encontrada.")

    else:
        musica.exibir()

def reproduzir_proxima(filas, historico):
    fila = escolher_fila(filas)

    if fila is None:
        return

    musica = fila.desenfileirar()

    if musica is None:
        print("Fila vazia. Não há música para reproduzir.")
        return

    print("Reproduzindo:")
    musica.exibir()

    historico.enfileirar(musica)

def exibir_fila(filas):
    fila = escolher_fila(filas)

    if fila is not None:
        fila.listar()

def estatisticas(biblioteca, filas, historico):
    print(f"Total na biblioteca: {biblioteca.total}")
    print(f"Relaxar: {filas['relaxar'].tamanho}")
    print(f"Focar: {filas['focar'].tamanho}")
    print(f"Animar: {filas['animar'].tamanho}")
    print(f"Treinar: {filas['treinar'].tamanho}")
    print(f"Histórico: {historico.tamanho}")

def menu():
    print("1 - Adicionar música")
    print("2 - Remover música")
    print("3 - Buscar música")
    print("4 - Listar biblioteca")
    print("5 - Montar fila de reprodução")
    print("6 - Reproduzir próxima")
    print("7 - Exibir fila de humor")
    print("8 - Exibir histórico")
    print("9 - Estatísticas")
    print("0 - Sair")


def main():
    biblioteca = Biblioteca()
    filas = criar_filas()
    historico = Fila()

    carregar_musicas(biblioteca)

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_musica(biblioteca)

        elif opcao == "2":
            remover_musica(biblioteca)

        elif opcao == "3":
            buscar_musica(biblioteca)

        elif opcao == "4":
            biblioteca.listar()

        elif opcao == "5":
            filas = montar_filas(biblioteca)

        elif opcao == "6":
            reproduzir_proxima(filas, historico)

        elif opcao == "7":
            exibir_fila(filas)

        elif opcao == "8":
            historico.listar()

        elif opcao == "9":
            estatisticas(biblioteca, filas, historico)

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")

        print()

main()