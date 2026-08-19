import random 
import time
import sys

sys.setrecursionlimit(100000)

from AP_03_ordenacao import(
    selection_sort,
    divide_and_conquer_sort,
    quick_sort
)

def gerar_caso_medio(n):
    return [random.randint(0,100000) for _ in range(n)]

def gerar_pior_caso(n):
    return list(range(n, 0 ,-1))

TAMANHOS = [100, 500, 1000, 5000]
REPETICOES = 50

ALGORITMOS = {
    "Selection Sort":
    selection_sort,
    "Merge Sort":
    divide_and_conquer_sort,
    "Quick Sort":
    quick_sort
}

def medir_tempo(algoritmo, lista, repeticoes):
    tempos = []
    for _ in range(repeticoes):
        entrada = lista.copy()

        inicio = time.perf_counter()

        algoritmo(entrada)

        fim = time.perf_counter()

        tempos.append(fim - inicio)

    return sum(tempos) / len(tempos)    

if __name__ == "__main__":
    print("="*80)
    print("BENCHMARK - ALGORITMOS DE ORDENAÇÃO")
    print("="*80)

    print(
        f"{'Algoritmo':<20}"
        f"{'N':<10}"
        f"{'Cenário':<15}"
        f"{'Tempo médio (s)':>20}"
    )

    print("-"*80)

    for n in TAMANHOS:
        for nome_cenario, gerador in [("Caso Médio", gerar_caso_medio), ("Pior Caso", gerar_pior_caso)]:
            lista = gerador(n)
            for nome_algoritmo, algoritmo in ALGORITMOS.items():
                tempo_medio = medir_tempo(
                    algoritmo,
                    lista, 
                    REPETICOES
                )
                print(
                    f"{nome_algoritmo:<20}"
                    f"{n:<10}"
                    f"{nome_cenario:<15}"
                    f"{tempo_medio:>20}"
                )  
             