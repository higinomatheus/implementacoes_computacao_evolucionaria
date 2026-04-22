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
    fitness_type = config["function"]
    elitismo = config.get("elitism", False)
    
    pop = gerar_populacao(pop_size)

    melhores = []
    medias = []

    for _ in range(generations):
        fit = [fitness(ind, fitness_type) for ind in pop]

        best_idx = fit.index(max(fit))
        melhor_individuo = pop[best_idx]
        melhor_fitness = fit[best_idx]

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
            
            if elitismo:
                # substitui o pior pelo melhor da geração anterior
                fit_nova = [fitness(ind, fitness_type) for ind in nova_pop]
                pior_idx = fit_nova.index(min(fit_nova))
                nova_pop[pior_idx] = melhor_individuo

        pop = nova_pop[:pop_size]

    fit = [fitness(ind) for ind in pop]
    melhor = max(fit)

    return {
        "melhor_fitness": melhor,
        "melhores": melhores,
        "medias": medias
    }