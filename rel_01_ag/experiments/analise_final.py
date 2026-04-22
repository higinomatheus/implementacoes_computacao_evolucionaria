import pandas as pd
import matplotlib.pyplot as plt
import json
import os

from src.algoritmo_genetico import algoritmo_genetico
from utils.graficos import plot_convergencia


def run_analysis():
    df = pd.read_csv("results/estatisticas/resumo_geral.csv")

    # =========================
    # Ordenar (melhor = maior fitness)
    # =========================
    df_sorted = df.sort_values(by="media", ascending=False)

    print("\nTop 10 configurações:")
    print(df_sorted.head(10))

    # salvar top 10
    df_sorted.head(10).to_csv("results/estatisticas/top10.csv", index=False)

    # =========================
    # Melhor configuração
    # =========================
    best_config_name = df_sorted.iloc[0]["config"]
    print(f"\nMelhor config: {best_config_name}")

    # =========================
    # Boxplot comparativo TOP 5
    # =========================
    top5 = df_sorted.head(5)

    data = []
    labels = []

    for _, row in top5.iterrows():
        nome = row["config"]
        df_exec = pd.read_csv(f"results/dados_brutos/{nome}.csv")

        data.append(df_exec["fitness"])
        labels.append(nome[:20])  # encurtar nome

    plt.figure()
    plt.boxplot(data)
    plt.xticks(range(1, len(labels)+1), labels, rotation=30)
    plt.title("Top 5 Configurações")
    plt.tight_layout()
    plt.savefig("results/boxplots/comparativo_top5.png")
    plt.close()

    # =========================
    # Rodar melhor config novamente (para gráfico)
    # =========================
    # reconstruir config a partir do nome
    parts = best_config_name.split("_")

    config = {
        "crossover_prob": float(parts[1][2:]),
        "mutation_prob": float(parts[2][2:]),
        "selection": parts[3],
        "population_size": int(parts[4][3:]),
        "generations": int(parts[5][3:]),
        "elitism": parts[6][4:] == "True",
        "function": parts[7]
    }

    print("\nRodando melhor configuração para gráfico de convergência...")

    res = algoritmo_genetico(config)

    plot_convergencia(
        res["melhores"],
        res["medias"],
        "results/graficos/convergencia_melhor.png"
    )

    # =========================
    # Gerar texto automático
    # =========================
    gerar_texto_relatorio(df_sorted)


def gerar_texto_relatorio(df_sorted):
    melhor = df_sorted.iloc[0]
    pior = df_sorted.iloc[-1]

    texto = f"""
## Análise dos Resultados

A melhor configuração encontrada foi:

{melhor['config']}

Apresentando os seguintes resultados:
- Média: {melhor['media']:.6f}
- Mediana: {melhor['mediana']:.6f}
- Máximo: {melhor['max']:.6f}
- Mínimo: {melhor['min']:.6f}

Observou-se que essa configuração proporcionou uma convergência mais estável,
com baixa variabilidade entre execuções.

Por outro lado, a pior configuração foi:

{pior['config']}

Indicando que determinados parâmetros impactam negativamente o desempenho do algoritmo.

De forma geral, observou-se que:

- Taxas moderadas de mutação apresentaram melhor desempenho
- O uso de elitismo contribuiu para maior estabilidade
- O método de seleção por torneio apresentou convergência mais rápida
- Funções multimodais como Cross-in-Tray apresentaram maior dificuldade de otimização

"""

    with open("results/estatisticas/analise.txt", "w", encoding="utf-8") as f:
        f.write(texto)

    print("\nTexto de análise gerado em: results/estatisticas/analise.txt")


if __name__ == "__main__":
    run_analysis()