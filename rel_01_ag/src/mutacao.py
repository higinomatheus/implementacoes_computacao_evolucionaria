import random

def mutacao(individuo, pm):
    novo = ""
    for bit in individuo:
        if random.random() < pm:
            novo += '1' if bit == '0' else '0'
        else:
            novo += bit
    return novo