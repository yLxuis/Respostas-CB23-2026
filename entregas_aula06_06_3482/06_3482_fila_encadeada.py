import importlib

PilhaEncadeada = importlib.import_module("06_3482_pilha_encadeada").PilhaEncadeada

class FilaEncadeada: 
    """Implementa o TAD fila usando duas instâncias de PilhaEncadeada. A pilha de entrada recebe novos elementos. A pilha de saída fornece os elementos pela frente da fila."""
    def __init__(self):
        """Cria uma fila vazia.
        Complexidade: O(1)."""
        self._entrada = PilhaEncadeada()
        self._saida = PilhaEncadeada()

    def enfileirar(self, item):
        """Insere um item no final da fila. O item é colocado na pilha de entrada.
        Complexidade: O(1)."""
        self._entrada.push(item)

    def _transferir(self):
        """Transfere os elementos da pilha de entrada para a pilha de saída. Essa operação só é chamada quando a pilha de saída está vazia.
        Complexidade: O(N)."""
        while not self._entrada.esta_vazia():
            self._saida.push(self._entrada.pop())

    def _garantir_saida(self):
        """Garante que a pilha de saída possua elementos quando a fila não estiver vazia.
        Complexidade: O(N) quando ocorre transferência e O(1) quanda a pilha de saída já possui elementos."""
        if self._saida.esta_vazia() and not self._entrada.esta_vazia():
            self._transferir()

    def desenfileirar(self):
        """Remove e retorna o elemento a frente da fila. Levanta IndexError se a fila estiver vazia.
        Complexidade: O(N) em uma chamada que exige transferência e O(1) armotizada."""
        if self.esta_vazia():
            raise IndexError("Não é possível remover de uma fila vazia.")
        self._garantir_saida()

        return self._saida.pop()

    def frente(self):
        """Retorna o elemento da frente, sem removê-lo. Levanta IndexError se a fila estiver vazia.
        Complexidade: O(N) em uma chamada que exige transferência e O(1) armotizada."""
        if self.esta_vazia():
            raise IndexError("Não é possível consultar a frente de uma fila vazia.")

        self._garantir_saida()

        return self._saida.topo()

    def esta_vazia(self):
        """Retorna True se a fila estiver vazia. A fila está vazia somente quando as duas pilhas estão vazias.
        Complexidade: O(1)."""

        return self._entrada.esta_vazia() and self._saida.esta_vazia()

    def len(self):
        """Retorna a quantidade de elementos armazenados na fila.
        Complexidade: O(1)."""

        return self._entrada.len() + self._saida.len()

    def repr(self):
        """Retorna uma representação textual da fila, da frente para o fim. A representação não altera o estado da fila.
        Complexidade: O(N)."""
        self._garantir_saida()

        resultado = "FilaEncadeada(["

        primeiro = True 

        temporaria = PilhaEncadeada()

        while not self._saida.esta_vazia():
            item = self._saida.pop()       

            if not primeiro:
                resultado += ", "

            resultado += repr(item)
            primeiro = False

            temporaria.push(item) 

        while not temporaria.esta_vazia():
            self._saida.push(temporaria.pop())

        entrada_temporaria = PilhaEncadeada()

        while not self._entrada.esta_vazia():
            entrada_temporaria.push(self._entrada.pop())

        elementos_entrada = PilhaEncadeada()

        while not entrada_temporaria.esta_vazia():
            item = entrada_temporaria.pop()
            elementos_entrada.push(item)

            if not primeiro:
                resultado += ", "

            resultado += repr(item)
            primeiro = False

        while not elementos_entrada.esta_vazia():
            self._entrada.push(elementos_entrada.pop())

        resultado += "])"

        return resultado

    def __repr__(self):
        """Permite usar repr(fila).
        Complexidade: O(N)."""
        return self.repr()
    
if __name__ == "__main__":
    fila = FilaEncadeada()

    fila.enfileirar(10)
    fila.enfileirar(20)
    fila.enfileirar(30)

    print(fila)
    print("Frente:", fila.frente())
    print("Desenfileirar:", fila.desenfileirar())
    print("Tamanho:", fila.len())
    print("Fila:", fila)
                               