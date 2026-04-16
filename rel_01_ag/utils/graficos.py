import matplotlib.pyplot as plt

def plot_convergencia(melhores, medias, path):
    plt.plot(melhores, label="Melhor")
    plt.plot(medias, label="Média")
    plt.legend()
    plt.savefig(path)
    plt.close()


def plot_boxplot(resultados, path):
    plt.boxplot(resultados)
    plt.savefig(path)
    plt.close()