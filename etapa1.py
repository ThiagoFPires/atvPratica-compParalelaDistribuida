import time


def tarefa(numero):
    resultado = 0

    for i in range(1, 300_000):
        resultado += (numero * i) % 97

    return resultado


def executar_sequencial(dados):
    inicio = time.perf_counter()

    resultados = []

    for numero in dados:
        resultados.append(tarefa(numero))

    fim = time.perf_counter()

    return resultados, fim - inicio


if __name__ == "__main__":
    dados = list(range(1, 101))

    resultados, tempo = executar_sequencial(dados)

    print("Tempo sequencial:", tempo)