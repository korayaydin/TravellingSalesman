import output
import plot
import travellingsales
import values


def calculate_travelling_sales_problem(coords):
    coordinates = travellingsales.give_coordinates(coords)
    fitness_problem = travellingsales.fitness_problem(len(coords), coordinates, False)
    best_way, best_fitness = travellingsales.find_bests(fitness_problem)
    output.write('Best way is: ', best_way)
    output.write('The fitness at the best state is: ', best_fitness)
    result = []
    for i in range(len(best_way)):
        result.append(values.Values.coordinate()[best_way[i]])
    return result


if __name__ == '__main__':
    given_coordinates = values.Values.coordinate()
    output.write('Given coordinates were: ', given_coordinates)

    print()
    plot.coordinate(calculate_travelling_sales_problem(given_coordinates))
