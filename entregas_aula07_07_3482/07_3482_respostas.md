# Aula 07 — Busca em Grafos e Labirintos

## Questão 1 — DFS iterativo

O código fornecido para a geração do labirinto utiliza uma busca em
profundidade (DFS) com retrocesso (backtracking). Na versão original,
a DFS é implementada de forma recursiva.

Nesta atividade, a recursão foi substituída por uma implementação
iterativa utilizando uma pilha explícita.

A posição inicial `(0, 0)` é inserida na pilha e marcada como visitada.
Enquanto a pilha não estiver vazia, a posição que está no topo é
analisada.

Caso exista uma sala vizinha ainda não visitada, a parede entre a sala
atual e essa nova sala é removida. A nova sala é então marcada como
visitada e inserida no topo da pilha.

Quando a posição atual não possui mais vizinhos não visitados, ela é
retirada da pilha. Esse procedimento representa o retrocesso
(backtracking): o algoritmo retorna para a sala anterior e continua
procurando outras salas ainda não visitadas.

Dessa forma, a pilha explícita desempenha o mesmo papel que a pilha de
chamadas utilizada implicitamente pela versão recursiva da DFS.

A implementação, portanto, mantém a estratégia de busca em profundidade
do código original, mas não utiliza chamadas recursivas.

---

## Questão 2 — Busca do caminho até o queijo

Para encontrar o caminho entre a posição inicial `(1,1)` e o queijo foi
utilizada uma busca em largura (BFS), implementada de forma iterativa.

A BFS utiliza uma fila para controlar a ordem em que as posições do
labirinto são exploradas. Inicialmente, a posição `(1,1)` é inserida na
fila.

A cada iteração, uma posição é retirada do início da fila e seus quatro
vizinhos são analisados: acima, abaixo, à esquerda e à direita.

Uma posição não pode ser visitada quando está fora dos limites do
labirinto, corresponde a uma parede ou já foi visitada anteriormente.

Para cada nova posição visitada, é armazenada a posição a partir da qual
ela foi alcançada. Essa informação é armazenada no dicionário `parent`.

Por exemplo, se uma posição `B` foi alcançada a partir de uma posição
`A`, é armazenada a relação:

    parent[B] = A

Quando o queijo é encontrado, o dicionário `parent` permite reconstruir
o caminho. A reconstrução começa na posição do queijo e percorre seus
predecessores até chegar à posição inicial `(1,1)`. Como esse processo
produz o caminho na ordem inversa, ele é posteriormente invertido.

### Justificativa da escolha da BFS

A BFS foi escolhida porque ela é adequada para encontrar o menor caminho
quando todos os movimentos possuem o mesmo custo.

Nesse labirinto, cada movimento de uma posição para uma posição vizinha
possui o mesmo custo. A BFS explora as posições em ordem crescente de
distância em relação à posição inicial. Portanto, quando o queijo é
alcançado, o caminho encontrado possui o menor número possível de
movimentos.

Uma DFS também seria capaz de encontrar um caminho até o queijo. Porém,
em um problema geral de busca de caminhos, a DFS não garante que o
primeiro caminho encontrado seja o menor.

Assim, a BFS é uma escolha mais adequada para a Questão 2 quando o
objetivo é encontrar um caminho mínimo.

---

## Relação com o labirinto perfeito

O gerador utilizado na atividade produz um labirinto perfeito. Isso
significa que existe exatamente um caminho entre quaisquer duas salas
do labirinto.

Consequentemente, neste labirinto específico, uma DFS também encontraria
o caminho existente entre `(1,1)` e o queijo.

Mesmo assim, a BFS foi utilizada na Questão 2 porque ela possui a
propriedade geral de encontrar caminhos mínimos em grafos não ponderados.
Isso torna explícita a escolha de uma estratégia apropriada para o
problema de encontrar o menor caminho.

---

## Comparação entre DFS e BFS

A DFS utiliza uma pilha e explora uma determinada possibilidade em
profundidade antes de retornar para explorar outras possibilidades.

Na implementação desta atividade, a DFS foi utilizada para a geração do
labirinto. A pilha explícita permite realizar o retrocesso necessário
sem utilizar recursão.

A BFS utiliza uma fila e explora os vértices por níveis de distância a
partir da posição inicial.

A principal diferença relevante para esta atividade é que a DFS não
garante, em geral, um caminho mínimo, enquanto a BFS garante o menor
caminho quando todas as arestas possuem o mesmo custo.

Por esse motivo, a DFS iterativa foi utilizada na Questão 1 e a BFS foi
utilizada para resolver o caminho até o queijo na Questão 2.