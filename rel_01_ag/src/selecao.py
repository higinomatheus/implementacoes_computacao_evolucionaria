import random

def roleta(pop, fitness):
    # Normalizar fitness para valores positivos
    min_fit = min(fitness)
    ajustado = [f - min_fit + 1e-6 for f in fitness]

    total = sum(ajustado)
    pick = random.uniform(0, total)

    current = 0
    for i, f in enumerate(ajustado):
        current += f
        if current > pick:
            return pop[i]

    # fallback (garantia)
    return pop[-1]


def torneio(pop, fitness, k=3):
    selected = random.sample(list(zip(pop, fitness)), k)
    selected.sort(key=lambda x: x[1], reverse=True)
    return selected[0][0]