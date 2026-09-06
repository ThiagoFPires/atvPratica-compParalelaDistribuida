import time
from concurrent.futures import ProcessPoolExecutor


def tarefa(numero):
    resultado = 0

    for i in range(1, 300_000):
        resultado += (numero * i) % 97

    return resultado


def executar_paralelo(dados, workers):
    inicio = time.perf_counter()

    with ProcessPoolExecutor(max_workers=workers) as executor:
        resultados = list(executor.map(tarefa, dados))

    fim = time.perf_counter()

    return resultados, fim - inicio


if __name__ == "__main__":
    dados = list(range(1, 101))

    for workers in [2, 4, 8]:

        _, tempo = executar_paralelo(dados, workers)

        print()
        print("Processos:", workers)
        print("Tempo:", tempo)