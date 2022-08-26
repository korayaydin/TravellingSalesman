import six
import sys

sys.modules['sklearn.externals.six'] = six
import mlrose


def give_coordinates(coordinates):
    return mlrose.TravellingSales(coords=coordinates)


def fitness_problem(length_coordinate, coordinates, maximize_choose):
    return mlrose.TSPOpt(length=length_coordinate, fitness_fn=coordinates,
                         maximize=maximize_choose)


def find_bests(problem):
    best_state, best_fitness = mlrose.genetic_alg(problem)
    return best_state, best_fitness
