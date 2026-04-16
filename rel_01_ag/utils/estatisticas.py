import numpy as np

def calcular_estatisticas(resultados):
    return {
        "media": np.mean(resultados),
        "mediana": np.median(resultados),
        "max": np.max(resultados),
        "min": np.min(resultados)
    }