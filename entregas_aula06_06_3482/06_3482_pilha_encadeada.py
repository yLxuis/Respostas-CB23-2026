class _No:
    """Representa um nó de uma lista simplesmente encadeada"""
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo


class PilhaEncadeada:
    """Implementa o TAD pilha usando uma lista simplesmente encadeada. A pilha mantém apenas uma referência para o topo e um contador de elementos"""
    def __init__(self):
        """Cria uma pilha vazia.
        Complexidade: O(1)."""
        self._topo = None
        self._tamanho = 0

    def push(self, item):
        """Insere um item no topo da pilha.
        Complexidade: O(1)."""
        novo_no = _No(item, self._topo)
        self._topo = novo_no
        self._tamanho += 1

    def pop(self):
        """Remove e retorna o item do topo da pilha.
        Complexidade: O(1)."""
        if self.esta_vazia():
            raise IndexError("Não é possível remover de uma pilha vazia.")

        item = self._topo.valor
        self._topo = self._topo.proximo
        self._tamanho -= 1

        return item

    def topo(self):
        """Retorna o item que está no topo, sem removê-lo.
        Complexidade: O(1)."""
        if self.esta_vazia():
            raise IndexError("Não é possível consultar o topo de uma lista vazia.")

        return self._topo.valor

    def esta_vazia(self):
        """Retorna True se a pilha estiver vazia e False caso contrário.
        Complexidade: O(1)."""
        return self._tamanho == 0

    def len(self):
        """Retorna a quantidade de elementos da pilha. O tamanho é mantido por um contador, portanto não é necessário percorrer os nós.
        Complexidade: O(1)."""
        return self._tamanho

    def repr(self):
        """Retorna uma representação textual da pilha, do topo para a base.
        Complexidade: O(N)."""

        resultado = "PilhaEncadeada(["

        atual = self._topo
        primeiro = True

        while atual is not None:
            if not primeiro:
                resultado += ","

            resultado += repr(atual.valor)

            primeiro = False
            atual = atual.proximo

        resultado += "])"

        return resultado

    def __repr__(self):
        """Permite usar repr(pilha).
        Complexidade: O(N)."""
        return self.repr()


if __name__ == "__main__":

    pilha = PilhaEncadeada()

    pilha.push(10)
    pilha.push(20)
    pilha.push(30)

    print(pilha)
    print("Topo:", pilha.topo())
    print("Pop:", pilha.pop())
    print("Tamanho:", pilha.len())
    print("Pilha:", pilha)