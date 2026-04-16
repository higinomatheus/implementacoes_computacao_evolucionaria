import json
import os
from src.algoritmo_genetico import algoritmo_genetico
from utils.estatisticas import calcular_estatisticas
from utils.graficos import plot_boxplot

def run():
    configs_path = "experiments/configs"
    results = []

    for file in os.listdir(configs_path):
        with open(os.path.join(configs_path, file)) as f:
            try:
                config = json.load(f)
            except Exception as e:
                print(f"Erro ao ler {file}: {e}")
                continue

        exec_results = []

        for _ in range(30):
            res = algoritmo_genetico(config)
            exec_results.append(res["melhor_fitness"])

        stats = calcular_estatisticas(exec_results)

        print(f"{file} -> {stats}")

        plot_boxplot(exec_results, f"results/boxplots/{file}.png")