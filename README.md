# Sistema de Playlist

Projeto desenvolvido para a disciplina de Estrutura de Dados.

O sistema simula o funcionamento básico de uma biblioteca de músicas e de filas de reprodução.  
A biblioteca utiliza lista encadeada simples para armazenar as músicas cadastradas.  
As filas de reprodução e o histórico utilizam fila FIFO implementada manualmente com nós encadeados.

## Funcionalidades

- Adicionar música
- Remover música
- Buscar música por ID
- Buscar música por título
- Listar biblioteca completa
- Montar filas de reprodução por humor usando BPM
- Exibir fila de humor
- Reproduzir próxima música por humor
- Adicionar música na fila de reprodução manual
- Ver fila de reprodução manual
- Reproduzir próxima música da fila de reprodução manual
- Exibir histórico de reproduções
- Exibir estatísticas do sistema

## Estruturas de Dados Utilizadas

### Lista Encadeada Simples

Utilizada para armazenar todas as músicas da biblioteca.

A lista encadeada permite percorrer as músicas a partir do primeiro nó, ligando uma música à próxima por meio de referências.

Classes utilizadas:
- Biblioteca
- NodoLista

### Fila FIFO

Utilizada para controlar a ordem de reprodução das músicas.

FIFO significa First In, First Out, ou seja, a primeira música que entra na fila é a primeira música que sai para ser reproduzida.

A fila FIFO é usada em:
- Filas de reprodução por humor
- Fila de reprodução manual
- Histórico de músicas reproduzidas

Classes utilizadas:
- Fila
- NodoFila

## Classes do Projeto

### Musica

Representa uma música cadastrada no sistema.

Atributos:
- id
- titulo
- artista
- genero
- bpm

### NodoLista

Representa um nó da lista encadeada simples.

Cada nó armazena:
- uma música
- a referência para o próximo nó

### Biblioteca

Representa a lista encadeada simples que armazena todas as músicas cadastradas.

Responsável por:
- adicionar músicas
- remover músicas
- buscar músicas por ID
- buscar músicas por título
- listar todas as músicas
- controlar o total de músicas
- controlar o próximo ID disponível

### NodoFila

Representa um nó da fila encadeada.

Cada nó armazena:
- uma música
- a referência para o próximo nó

### Fila

Representa uma fila FIFO encadeada.

Responsável por:
- enfileirar músicas
- desenfileirar músicas
- listar músicas da fila
- controlar o tamanho da fila

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

## Como Executar

Para executar o projeto, siga o passo a passo abaixo.

### 1. Abrir o Prompt de Comando

No Windows, pesquise por:

```text
Prompt de Comando
```

ou:

```text
cmd
```

Depois, abra o terminal.

### 2. Escolher onde o projeto será salvo

Entre na pasta onde deseja salvar o projeto.

Exemplo:

```bash
cd Desktop
```

ou:

```bash
cd Documents
```

Também é possível digitar:

```bash
cd 
```

com um espaço depois do `cd` e apertar a tecla `Tab` para o terminal mostrar as pastas disponíveis.

Continue apertando `Tab` até encontrar a pasta desejada.  
Quando a pasta correta aparecer, pressione `Enter`.

### 3. Clonar o repositório

Depois de entrar na pasta escolhida, clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/sistema_playlist.git
```

### 4. Entrar na pasta do projeto

Após clonar, entre na pasta do projeto:

```bash
cd sistema_playlist
```

### 5. Executar o sistema

Com o terminal dentro da pasta do projeto, execute:

```bash
python main.py
```

Caso o comando acima não funcione, tente:

```bash
py main.py
```

### Resumo dos comandos

```bash
cd Desktop
git clone https://github.com/SEU_USUARIO/sistema_playlist.git
cd sistema_playlist
python main.py
```

Caso necessário:

```bash
py main.py
```