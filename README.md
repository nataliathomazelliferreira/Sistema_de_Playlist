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


## Como Executar

Para executar o projeto, primeiro abra o Prompt de Comando do Windows.

No Windows, você pode fazer isso pesquisando por:

```text
Prompt de Comando

ou

cmd

Depois de abrir o Prompt de Comando, escolha a pasta onde deseja salvar o projeto.

Para entrar em uma pasta, use o comando:

cd nome_da_pasta

Uma dica é digitar:

cd 

com um espaço depois do cd, e apertar a tecla Tab no teclado.
O próprio terminal vai completando ou mostrando as pastas disponíveis.

Se não aparecer a pasta desejada, continue apertando Tab até encontrar.

Exemplo:

cd Desktop

ou:

cd Documents

Depois que estiver dentro da pasta onde deseja salvar o projeto, clone o repositório:

git clone https://github.com/SEU_USUARIO/sistema_playlist.git

Em seguida, entre na pasta do projeto:

cd sistema_playlist

Agora execute o sistema:

python main.py

Se o comando python main.py não funcionar, tente:

py main.py

Resumo dos comandos:

cd Desktop
git clone https://github.com/SEU_USUARIO/sistema_playlist.git
cd sistema_playlist
python main.py

ou, se necessário:

py main.py

