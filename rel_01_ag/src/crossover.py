import random

def crossover(p1, p2, pc):
    if random.random() > pc:
        return p1, p2

    cut_x = random.randint(1, 15)
    cut_y = random.randint(17, 31)

    child1 = (
        p1[:cut_x] + p2[cut_x:16] +
        p1[16:cut_y] + p2[cut_y:]
    )

    child2 = (
        p2[:cut_x] + p1[cut_x:16] +
        p2[16:cut_y] + p1[cut_y:]
    )

    return child1, child2