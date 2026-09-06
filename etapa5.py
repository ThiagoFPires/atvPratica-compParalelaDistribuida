import time
from concurrent.futures import ProcessPoolExecutor


def tarefa(numero):
    resultado = 0

    for i in range(1, 300_000):
        resultado += (numero * i) % 97

    return resultado


def executar_sequencial(dados):
    inicio = time.perf_counter()

    for numero in dados:
        tarefa(numero)

    fim = time.perf_counter()

    return fim - inicio


def executar_paralelo(dados, workers):
    inicio = time.perf_counter()

    with ProcessPoolExecutor(max_workers=workers) as executor:
        list(executor.map(tarefa, dados))

    fim = time.perf_counter()

    return fim - inicio


if __name__ == "__main__":

    experimentos = [20, 100, 500]

    for quantidade in experimentos:

        dados = list(range(1, quantidade + 1))

        tempo_sequencial = executar_sequencial(dados)

        print("\n==============================")
        print("Número de tarefas:", quantidade)
        print("Tempo sequencial:", tempo_sequencial)

        for workers in [2, 4, 8]:

            tempo_paralelo = executar_paralelo(dados, workers)

            speedup = tempo_sequencial / tempo_paralelo
            eficiencia = speedup / workers

            print("\nProcessos:", workers)
            print("Tempo:", tempo_paralelo)
            print("Speedup:", speedup)
            print("Eficiência:", eficiencia)