import itertools
import os
import pandas as pd

from src.algoritmo_genetico import algoritmo_genetico
from utils.estatisticas import calcular_estatisticas
from utils.graficos import plot_boxplot


def run():
    # =========================
    # Parâmetros
    # =========================
    pcs = [0.6, 0.8, 1.0]
    pms = [0.01, 0.05, 0.1]
    selecoes = ["roleta", "torneio"]
    pops = [20, 50, 100]
    gens = [50, 100]
    elitisms = [True, False]
    funcoes = ["cross", "drop"]

    combinacoes = list(itertools.product(
        pcs, pms, selecoes, pops, gens, elitisms, funcoes
    ))

    print(f"Total de combinações: {len(combinacoes)}")

    resumo_geral = []

    # =========================
    # Loop principal
    # =========================
    for i, (pc, pm, sel, pop, gen, elit, func) in enumerate(combinacoes):

        config = {
            "crossover_prob": pc,
            "mutation_prob": pm,
            "selection": sel,
            "population_size": pop,
            "generations": gen,
            "elitism": elit,
            "function": func
        }

        exec_results = []

        for _ in range(30):
            res = algoritmo_genetico(config)
            exec_results.append(res["melhor_fitness"])

        # =========================
        # Estatísticas
        # =========================
        stats = calcular_estatisticas(exec_results)

        # =========================
        # Nome da configuração
        # =========================
        nome = f"{i}_pc{pc}_pm{pm}_{sel}_pop{pop}_gen{gen}_elit{elit}_{func}"

        print(f"[{i+1}/{len(combinacoes)}] {nome} -> {stats}")

        # =========================
        # Salvar CSV
        # =========================
        df = pd.DataFrame(exec_results, columns=["fitness"])
        df.to_csv(f"results/dados_brutos/{nome}.csv", index=False)

        # =========================
        # Boxplot individual
        # =========================
        plot_boxplot(exec_results, f"results/boxplots/{nome}.png")

        # =========================
        # Resumo geral
        # =========================
        resumo_geral.append({
            "config": nome,
            **stats
        })

    # =========================
    # Salvar resumo geral
    # =========================
    df_resumo = pd.DataFrame(resumo_geral)
    df_resumo.to_csv("results/estatisticas/resumo_geral.csv", index=False)

    print("\nExperimentos finalizados!")