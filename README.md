# Sistema-de-Playlist

Projeto desenvolvido para a disciplina de Estrutura de Dados.

O sistema utiliza lista encadeada simples para armazenar músicas da biblioteca e filas FIFO encadeadas para gerenciamento das filas de reprodução e histórico.

## Funcionalidades

- Adicionar música
- Remover música
- Buscar música por id
- Buscar música por título
- Listar biblioteca
- Montar filas de reprodução por BPM
- Reproduzir músicas
- Exibir filas
- Exibir histórico
- Exibir estatísticas

## Estruturas de Dados Utilizadas

### Lista Encadeada

Utilizada para armazenar a biblioteca de músicas.

Classes:
- Biblioteca
- NodoLista

### Fila FIFO

Utilizada para:
- Filas de reprodução
- Histórico de músicas reproduzidas

Classes:
- Fila
- NodoFila

## Organização do Projeto

```text
sistema_playlist/
│
├── .gitignore
├── README.md
├── main.py
├── musica.py
├── lista.py
├── fila.py
├── biblioteca.py
└── musicas.txt
```

## Como executar

Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/sistema_playlist.git
```

Entre na pasta do projeto:

```bash
cd sistema_playlist
```

Execute o sistema:

```bash
python main.py
```

## Funcionamento das Filas

As músicas são separadas automaticamente de acordo com o BPM.

| Fila | BPM |
|---|---|
| Relaxar | até 80 |
| Focar | 81 a 120 |
| Animar | 121 a 160 |
| Treinar | acima de 160 |

## Requisitos Atendidos

- Lista encadeada implementada manualmente
- Filas implementadas manualmente
- Sem uso de list/deque para filas ou lista encadeada
- Histórico usando estrutura Fila
- IDs automáticos
- IDs não reutilizados
- Tratamento de entradas inválidas
- Remontagem das filas a cada execução da operação
