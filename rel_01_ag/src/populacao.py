import random

def gerar_individuo():
    return ''.join(random.choice(['0', '1']) for _ in range(32))


def gerar_populacao(tamanho):
    return [gerar_individuo() for _ in range(tamanho)]