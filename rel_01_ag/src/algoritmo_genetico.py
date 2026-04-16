from .populacao import gerar_populacao
from .fitness import fitness
from .selecao import roleta, torneio
from .crossover import crossover
from .mutacao import mutacao


def algoritmo_genetico(config):
    pop_size = config["population_size"]
    generations = config["generations"]
    pc = config["crossover_prob"]
    pm = config["mutation_prob"]
    selection_type = config["selection"]

    pop = gerar_populacao(pop_size)

    melhores = []
    medias = []

    for _ in range(generations):
        fit = [fitness(ind) for ind in pop]

        melhores.append(max(fit))
        medias.append(sum(fit) / len(fit))

        nova_pop = []

        while len(nova_pop) < pop_size:
            if selection_type == "roleta":
                p1 = roleta(pop, fit)
                p2 = roleta(pop, fit)
            else:
                p1 = torneio(pop, fit)
                p2 = torneio(pop, fit)

            f1, f2 = crossover(p1, p2, pc)

            f1 = mutacao(f1, pm)
            f2 = mutacao(f2, pm)

            nova_pop.extend([f1, f2])

        pop = nova_pop[:pop_size]

    fit = [fitness(ind) for ind in pop]
    melhor = max(fit)

    return {
        "melhor_fitness": melhor,
        "melhores": melhores,
        "medias": medias
    }