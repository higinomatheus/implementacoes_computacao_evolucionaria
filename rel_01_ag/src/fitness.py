import math
from .representacao import decode_individuo

def rastrigin(individuo):
    x, y = decode_individuo(individuo)
    return 20 + x**2 + y**2 - 10 * (math.cos(2*math.pi*x) + math.cos(2*math.pi*y))


def fitness(individuo):
    # Maximização → inverter sinal da Rastrigin
    return -rastrigin(individuo)