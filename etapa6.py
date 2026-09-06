import time
from concurrent.futures import ProcessPoolExecutor


def tarefa(numero):

    if numero % 10 == 0:
        limite = 1_500_000
    else:
        limite = 300_000

    resultado = 0

    for i in range(1, limite):
        resultado += (numero * i) % 97

    return resultado


def executar_sequencial(dados):
    inicio = time.perf_counter()

    resultados = []

    for numero in dados:
        resultados.append(tarefa(numero))

    fim = time.perf_counter()

    return resultados, fim - inicio


def executar_paralelo(dados, workers):
    inicio = time.perf_counter()

    with ProcessPoolExecutor(max_workers=workers) as executor:
        resultados = list(executor.map(tarefa, dados))

    fim = time.perf_counter()

    return resultados, fim - inicio


if __name__ == "__main__":

    dados = list(range(1, 101))

    # Sequencial
    _, tempo_sequencial = executar_sequencial(dados)

    print("Tempo sequencial:", tempo_sequencial)

    # Paralelo
    for workers in [2, 4, 8]:

        _, tempo_paralelo = executar_paralelo(dados, workers)

        speedup = tempo_sequencial / tempo_paralelo
        eficiencia = speedup / workers

        print("\nProcessos:", workers)
        print("Tempo:", tempo_paralelo)
        print("Speedup:", speedup)
        print("Eficiência:", eficiencia)