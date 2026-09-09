import importlib
import unittest

PilhaEncadeada = importlib.import_module("06_3482_pilha_encadeada").PilhaEncadeada

FilaEncadeada = importlib.import_module("06_3482_fila_encadeada").FilaEncadeada

class TestPilhaEncadeada(unittest.TestCase):

    def test_pilha_vazia_inicialmente(self):
        pilha = PilhaEncadeada()

        self.assertTrue(pilha.esta_vazia())
        self.assertEqual(pilha.len(), 0)

    def test_ordem_lifo(self):
        pilha = PilhaEncadeada()

        pilha.push(1)
        pilha.push(2)
        pilha.push(3)

        self.assertEqual(pilha.pop(), 3)
        self.assertEqual(pilha.pop(), 2)
        self.assertEqual(pilha.pop(), 1)

        self.assertTrue(pilha.esta_vazia())

    def test_topo_sem_remover(self):
        pilha = PilhaEncadeada()

        pilha.push(10)
        pilha.push(20)

        self.assertEqual(pilha.topo(), 20)
        self.assertEqual(pilha.len(), 2)
        self.assertEqual(pilha.topo(), 20)

    def test_pop_em_pilha_vazia(self):
        pilha = PilhaEncadeada()

        with self.assertRaises(IndexError):
            pilha.pop()

    def test_topo_em_pilha_vazia(self):
        pilha = PilhaEncadeada()

        with self.assertRaises(IndexError):
            pilha.topo()

    def test_len_apos_insercoes_e_remocoes(self):
        pilha = PilhaEncadeada()

        self.assertEqual(pilha.len(), 0)

        pilha.push("A")
        self.assertEqual(pilha.len(), 1)

        pilha.push("B")
        self.assertEqual(pilha.len(), 2)

        pilha.push("C")
        self.assertEqual(pilha.len(), 3)

        pilha.pop()
        self.assertEqual(pilha.len(), 2)

        pilha.pop()
        self.assertEqual(pilha.len(), 1)

        pilha.pop()
        self.assertEqual(pilha.len(), 0)

    def test_alternancia_de_operacoes(self):
        pilha = PilhaEncadeada()

        pilha.push(1)
        pilha.push(2)

        self.assertEqual(pilha.pop(), 2)

        pilha.push(3)

        self.assertEqual(pilha.pop(), 3)
        self.assertEqual(pilha.pop(), 1)

        self.assertTrue(pilha.esta_vazia())

    def test_tipos_diferentes_none_repetidos(self):
        pilha = PilhaEncadeada()

        pilha.push(10)
        pilha.push("texto")
        pilha.push(None)
        pilha.push(10)

        self.assertEqual(pilha.pop(), 10)
        self.assertIsNone(pilha.pop())
        self.assertEqual(pilha.pop(), "texto")
        self.assertEqual(pilha.pop(), 10)

    def test_repr_pilha(self):
        pilha = PilhaEncadeada()

        pilha.push(1)
        pilha.push(2)
        pilha.push(3)

        representacao = pilha.repr()

        self.assertIn("3", representacao)
        self.assertIn("2", representacao)
        self.assertIn("1", representacao)

class TestFilaEncadeada(unittest.TestCase):

    def test_fila_vazia_inicialmente(self):
        fila = FilaEncadeada()

        self.assertTrue(fila.esta_vazia())
        self.assertEqual(fila.len(), 0)

    def test_ordem_fifo(self):
        fila = FilaEncadeada()

        fila.enfileirar(1)
        fila.enfileirar(2)
        fila.enfileirar(3)

        self.assertEqual(fila.desenfileirar(), 1)
        self.assertEqual(fila.desenfileirar(), 2)
        self.assertEqual(fila.desenfileirar(), 3)

        self.assertTrue(fila.esta_vazia())

    def test_intercalacao_enfileirar_desenfileirar(self):
        fila = FilaEncadeada()

        fila.enfileirar("A")
        fila.enfileirar("B")

        self.assertEqual(fila.desenfileirar(), "A")

        fila.enfileirar("C")

        self.assertEqual(fila.desenfileirar(), "B")

        fila.enfileirar("D")

        self.assertEqual(fila.desenfileirar(), "C")
        self.assertEqual(fila.desenfileirar(), "D")

    def test_esvaziar_e_reutilizar(self):
        fila = FilaEncadeada()

        fila.enfileirar(1)
        fila.enfileirar(2)

        self.assertEqual(fila.desenfileirar(), 1)
        self.assertEqual(fila.desenfileirar(), 2)

        self.assertTrue(fila.esta_vazia())

        fila.enfileirar(3)
        fila.enfileirar(4)

        self.assertEqual(fila.desenfileirar(), 3)
        self.assertEqual(fila.desenfileirar(), 4)

        self.assertTrue(fila.esta_vazia())

    def test_desenfileirar_fila_vazia(self):
        fila = FilaEncadeada()

        with self.assertRaises(IndexError):
            fila.desenfileirar()

    def test_frente_fila_vazia(self):
        fila = FilaEncadeada()

        with self.assertRaises(IndexError):
            fila.frente()

    def test_frente_sem_remover(self):
        fila = FilaEncadeada()

        fila.enfileirar(10)
        fila.enfileirar(20)

        self.assertEqual(fila.frente(), 10)
        self.assertEqual(fila.len(), 2)
        self.assertEqual(fila.frente(), 10)

    def test_len_da_fila(self):
        fila = FilaEncadeada()

        self.assertEqual(fila.len(), 0)

        fila.enfileirar(1)
        self.assertEqual(fila.len(), 1)

        fila.enfileirar(2)
        self.assertEqual(fila.len(), 2)

        fila.enfileirar(3)
        self.assertEqual(fila.len(), 3)

        fila.desenfileirar()
        self.assertEqual(fila.len(), 2)

        fila.desenfileirar()
        self.assertEqual(fila.len(), 1)

        fila.desenfileirar()
        self.assertEqual(fila.len(), 0)

    def test_repr_fila(self):
        fila = FilaEncadeada()

        fila.enfileirar(1)
        fila.enfileirar(2)
        fila.enfileirar(3)

        representacao = fila.repr()

        self.assertIn("1", representacao)
        self.assertIn("2", representacao)
        self.assertIn("3", representacao)

if __name__ == "__main__":
    unittest.main()
