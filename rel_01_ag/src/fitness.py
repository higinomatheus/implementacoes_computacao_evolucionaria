import math
from .representacao import decode_individuo

def cross_in_tray(x, y):
    term1 = math.sin(x) * math.sin(y)
    term2 = math.exp(abs(100 - (math.sqrt(x**2 + y**2) / math.pi)))
    
    result = -0.0001 * (abs(term1 * term2) + 1) ** 0.1
    return result

def drop_wave(x, y):
    r = math.sqrt(x**2 + y**2)
    
    numerator = 1 + math.cos(12 * r)
    denominator = 0.5 * (x**2 + y**2) + 2
    
    result = - numerator / denominator
    return result

def fitness(individuo, func="cross"):
    x, y = decode_individuo(individuo)

    if func == "cross":
        return -cross_in_tray(x, y)
    elif func == "drop":
        return -drop_wave(x, y)