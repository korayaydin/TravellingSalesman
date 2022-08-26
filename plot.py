import matplotlib.pyplot as plt


def coordinate(r):
    plt.plot(*zip(*r), '-o')
    plt.show()
