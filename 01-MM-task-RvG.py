import copy
import random
import sys


class Cell:
    def __init__(self, x1, x2, generations=0):
        self.x1 = x1
        self.x2 = x2
        self.generations = generations


def draw_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()


def default_matrix_filling():
    for i in range(rows):
        matrix.append([])
        for j in range(columns):
            number = random.randint(0, 1)
            matrix[i].append(number)   # filling each cell with 1 or 0
    try:
        if matrix[searched_row][searched_col] == 1:
            square.generations += 1        # incrementing green counts at searched cell
    except IndexError as e:
        print("Sorry, searched cell is out of the grid.")
        sys.exit(1)


def transform_matrix_once(matrix):

    mutated_matrix = copy.deepcopy(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            g_neighbours = find_neighbours(i, j)
            if matrix[i][j] == 0:    # RED
                if g_neighbours == 3 or g_neighbours == 6:
                    mutated_matrix[i][j] = 1   # red -> green
            else:                    # GREEN
                if g_neighbours == 0 or \
                        g_neighbours == 1 or \
                        g_neighbours == 4 or \
                        g_neighbours == 5 or \
                        g_neighbours == 7 or \
                        g_neighbours == 8:
                    mutated_matrix[i][j] = 0   # green -> red

    if mutated_matrix[searched_row][searched_col] == 1:
        square.generations += 1

    return mutated_matrix


def find_neighbours(x, y):
    neighbours = []
    for x2 in range(x - 1, x + 2):
        for y2 in range(y - 1, y + 2):
            if (0 <= x < rows) and (0 <= y < columns) \
                    and (x != x2 or y != y2) \
                    and (0 <= x2 < rows) \
                    and (0 <= y2 < columns):
                neighbours.append((x2, y2))    # adding each neighbour to the list

    green_neighbours = 0

    for t in neighbours:    # iterating through each tuple in neighbours
        left = t[0]
        right = t[1]
        if matrix[left][right] == 1:
            green_neighbours += 1

    return green_neighbours


# def iterate_matrix_n_times(n, matrix): # TODO PRINTS ALL THE SAME MATRICES
#
#     iterable_matrix = matrix       # initialize variable to help iterations
#     matrix1 = matrix
#     for i in range(n):
#         # iterable_matrix = transform_matrix_once(iterable_matrix)
#         matrix1 = transform_matrix_once(iterable_matrix)
#         iterable_matrix = copy.deepcopy(matrix1)
#         print(iterable_matrix)
#
#     return iterable_matrix


dimensions = list(map(int, input().split(", ")))

rows = dimensions[0]
columns = dimensions[1]

wanted_coordinates_and_generation = list(map(int, input().split(", ")))

""" Switched sides of rows and columns of the searched cell to match 
the requirements of the "Example 1" in the task in order [1,0] to be 
top center cell of 3x3 grid"""

searched_row = wanted_coordinates_and_generation[1]
searched_col = wanted_coordinates_and_generation[0]
searched_generations = wanted_coordinates_and_generation[2]

square = Cell(searched_col, searched_row)

matrix = []
default_matrix_filling()

# draw_matrix(matrix)   # Draws Generation 0 matrix
# print()

# matrix = transform_matrix_once(matrix)   # saving the result between iterations
# print(matrix)

for i in range(searched_generations):
    matrix = transform_matrix_once(matrix)
    # print(matrix)

# last_gen_matrix = iterate_matrix_n_times(searched_generations, matrix) # TODO NEEDS FIX
# print(last_gen_matrix)
print(f"Cell [{searched_col},{searched_row}] has been green {square.generations} times")
