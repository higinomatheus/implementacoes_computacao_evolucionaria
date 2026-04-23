# experiments/boxplots_parametros.py
import os
import pandas as pd
import matplotlib.pyplot as plt

RESUMO = "results/estatisticas/resumo_geral.csv"
RAW_DIR = "results/dados_brutos"
OUT_DIR = "results/boxplots"

def extrair_parametros(nome):
    parts = nome.split("_")
    return {
        "pc": parts[1][2:],
        "pm": parts[2][2:],
        "selecao": parts[3],
        "populacao": parts[4][3:],
        "geracoes": parts[5][3:],
        "elitismo": parts[6][4:],
        "funcao": parts[7]
    }

def carregar_todos():
    resumo = pd.read_csv(RESUMO)
    registros = []

    for _, row in resumo.iterrows():
        nome = row["config"]
        caminho = os.path.join(RAW_DIR, f"{nome}.csv")
        df = pd.read_csv(caminho)

        params = extrair_parametros(nome)
        for val in df["fitness"]:
            registros.append({
                "config": nome,
                "fitness": val,
                **params
            })

    return pd.DataFrame(registros)

def gerar_boxplot(df, coluna, arquivo, titulo):
    grupos = sorted(df[coluna].unique(), key=lambda x: str(x))
    data = [df[df[coluna] == g]["fitness"] for g in grupos]

    plt.figure(figsize=(8, 5))
    plt.boxplot(data, labels=grupos)
    plt.title(titulo)
    plt.ylabel("Fitness")
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, arquivo))
    plt.close()

def main():
    df = carregar_todos()

    gerar_boxplot(df, "pc", "boxplot_pc.png", "Impacto da probabilidade de cruzamento")
    gerar_boxplot(df, "pm", "boxplot_pm.png", "Impacto da probabilidade de mutação")
    gerar_boxplot(df, "selecao", "boxplot_selecao.png", "Impacto do método de seleção")
    gerar_boxplot(df, "populacao", "boxplot_populacao.png", "Impacto do tamanho da população")
    gerar_boxplot(df, "geracoes", "boxplot_geracoes.png", "Impacto do número de gerações")
    gerar_boxplot(df, "elitismo", "boxplot_elitismo.png", "Impacto do elitismo")

if __name__ == "__main__":
    main()