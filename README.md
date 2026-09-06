# Atividade Prática 01 - Programação Paralela

Repositório com a implementação prática e análise experimental de computação concorrente e paralela em Python utilizando `concurrent.futures.ProcessPoolExecutor`.

---

## 📁 Estrutura de Arquivos

* **`etapa1.py`**: Implementação sequencial da tarefa computacional para cálculo do tempo base ($T_1$).
* **`etapa2.py`**: Versão paralela utilizando múltiplos processos (2, 4 e 8 workers).
* **`etapa3.py`**: Script para cálculo de Speedup e Eficiência a partir dos tempos medidos.
* **`etapa5.py`**: Testes comparativos de granularidade variando a quantidade de tarefas (20, 100 e 500 itens).
* **`etapa6.py`**: Experimento de balanceamento de carga com tarefas de tempo heterogêneo.
* **`relatorio_atividade_pratica_01.txt`**: Relatório com o registro das métricas e respostas detalhadas das Etapas 1 a 6.

---

## ⚙️ Como Executar

Para executar qualquer um dos experimentos, basta utilizar o Python 3:

```bash
# Execução sequencial (Etapa 1)
python etapa1.py

# Execução paralela (Etapa 2)
python etapa2.py

# Experimento de granularidade (Etapa 5)
python etapa5.py

# Experimento de balanceamento de carga (Etapa 6)
python etapa6.py
```
