# Análise de Complexidade

## Questão 1 — Pilha Encadeada

A pilha é implementada utilizando uma lista simplesmente encadeada. Cada nó possui um valor e uma referência para o próximo nó.

A classe `PilhaEncadeada` mantém uma referência para o nó que está no topo e um contador com a quantidade de elementos.

### push(item)

A operação `push` cria um novo nó e faz com que ele aponte para o antigo topo. Em seguida, a referência `_topo` passa a apontar para o novo nó.

Como nenhuma parte da lista precisa ser percorrida, a operação possui complexidade:

**O(1)**.

### pop()

A operação `pop` acessa diretamente o nó do topo, guarda seu valor, atualiza `_topo` para o próximo nó e decrementa o contador.

Nenhum percurso pela lista é necessário.

Portanto:

**O(1)**.

### topo()

A operação `topo` apenas acessa o valor armazenado no nó apontado por `_topo`.

Portanto:

**O(1)**.

### esta_vazia()

A operação verifica se o contador de elementos é igual a zero.

Portanto:

**O(1)**.

### len()

A quantidade de elementos não é obtida percorrendo a lista. O valor é mantido em um contador atualizado a cada `push` e `pop`.

Assim:

**O(1)**.

### repr()

Para produzir a representação textual da pilha, é necessário percorrer os nós desde o topo até o final da lista.

Para N elementos, são visitados N nós.

Portanto:

**O(N)**.

---

# Questão 2 — Fila Encadeada

A fila é implementada por composição utilizando duas instâncias de `PilhaEncadeada`.

Uma pilha é chamada de pilha de entrada e a outra de pilha de saída.

A pilha de entrada recebe os novos elementos. Quando é necessário remover ou consultar a frente da fila e a pilha de saída está vazia, todos os elementos da entrada são transferidos para a saída.

Essa inversão faz com que o elemento que chegou primeiro fique no topo da pilha de saída.

## enfileirar(item)

O novo elemento é inserido diretamente na pilha de entrada através da operação `push`.

Como `push` é O(1):

**O(1)**.

## desenfileirar()

Se a pilha de saída possuir elementos, basta realizar um `pop`, que possui custo O(1).

Caso a pilha de saída esteja vazia, todos os elementos da pilha de entrada precisam ser transferidos para a pilha de saída. Se existirem N elementos, essa transferência custa O(N).

Portanto, uma chamada isolada de `desenfileirar` pode custar:

**O(N)** no pior caso.

Entretanto, a complexidade amortizada é:

**O(1)**.

Isso ocorre porque cada elemento é transferido da pilha de entrada para a pilha de saída no máximo uma vez durante sua permanência na fila.

Assim, cada elemento sofre, no máximo:

1. uma operação de `push` na pilha de entrada;
2. uma operação de `pop` da pilha de entrada e uma operação de `push` na pilha de saída durante a transferência;
3. uma operação de `pop` na pilha de saída quando for removido da fila.

Portanto, embora uma única chamada possa realizar N transferências, essas transferências não serão repetidas para os mesmos elementos.

Para N elementos, o número total de operações de transferência ao longo de toda a sequência é proporcional a N. Consequentemente, distribuindo esse custo pelas N operações de remoção:

**O(N) / N = O(1)**.

Logo, `desenfileirar` possui custo **O(N) no pior caso de uma chamada isolada**, mas **O(1) amortizada**.

## frente()

A operação `frente` utiliza a mesma estratégia de `desenfileirar`.

Se a pilha de saída estiver vazia, pode ser necessário transferir N elementos, produzindo custo O(N) naquela chamada.

Depois da transferência, entretanto, a consulta ao topo da pilha de saída é O(1).

Assim, considerando a sequência de operações, a complexidade amortizada é:

**O(1)**.

## esta_vazia()

A fila está vazia quando tanto a pilha de entrada quanto a pilha de saída estão vazias.

Como `esta_vazia()` da pilha é O(1), temos:

**O(1)**.

## len()

A quantidade de elementos da fila é obtida pela soma da quantidade de elementos presentes nas duas pilhas:

`entrada.len() + saida.len()`

Como `len()` da pilha é O(1), a operação também é:

**O(1)**.

## repr()

A representação da fila precisa apresentar os elementos na ordem FIFO, da frente para o fim.

Para isso, os elementos podem ser percorridos utilizando somente a interface pública de `PilhaEncadeada`, preservando o estado da fila.

Como é necessário processar cada elemento pelo menos uma vez, a complexidade é:

**O(N)**.

---

# Resumo

| Operação             |                     Complexidade |
| -------------------- | -------------------------------: |
| Pilha `push`         |                             O(1) |
| Pilha `pop`          |                             O(1) |
| Pilha `topo`         |                             O(1) |
| Pilha `esta_vazia`   |                             O(1) |
| Pilha `len`          |                             O(1) |
| Pilha `repr`         |                             O(N) |
| Fila `enfileirar`    |                             O(1) |
| Fila `desenfileirar` | O(N) pior caso / O(1) amortizada |
| Fila `frente`        | O(N) pior caso / O(1) amortizada |
| Fila `esta_vazia`    |                             O(1) |
| Fila `len`           |                             O(1) |
| Fila `repr`          |                             O(N) |
