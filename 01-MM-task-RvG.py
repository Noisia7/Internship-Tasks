import copy
import random
import sys


class Cell:
    def __init__(self, x1, x2, generations=0):
        self.x1 = x1
        self.x2 = x2
        self.generations = generations


class Matrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []

    """================================================================="""
    """             Filling the matrix with ones and zeros              """
    """  Incrementing green counts at searched cell if color is green   """
    """       Exiting program if searched cell is out of range          """
    """================================================================="""

    def default_matrix_filling(self, square):
        for i in range(self.width):
            self.cells.append([])
            for j in range(self.height):
                number = random.randint(0, 1)
                self.cells[i].append(number)
        try:
            if self.cells[searched_row][searched_col] == 1:
                square.generations += 1
        except IndexError as e:
            print("Sorry, searched cell is out of the grid.")
            sys.exit(1)

    def draw_matrix(self):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                print(self.cells[i][j], end=" ")
            print()

    def find_neighbours(self, x, y):

        neighbours = []

        """================================================="""
        """       Adding each neighbour to the list         """
        """================================================="""

        for x2 in range(x - 1, x + 2):
            for y2 in range(y - 1, y + 2):
                if (0 <= x < rows) and (0 <= y < columns) \
                        and (x != x2 or y != y2) \
                        and (0 <= x2 < rows) \
                        and (0 <= y2 < columns):
                    neighbours.append((x2, y2))

        green_neighbours = 0

        """========================================================="""
        """       Iterating through each tuple in neighbours        """
        """========================================================="""
        for t in neighbours:
            left = t[0]
            right = t[1]
            if self.cells[left][right] == 1:
                green_neighbours += 1

        return green_neighbours

    def transform_matrix_once(self):

        """======================================================"""
        """      Creating new matrix to save changed values      """
        """======================================================"""

        mutated_matrix = copy.deepcopy(self.cells)

        for i in range(len(self.cells[0])):
            for j in range(len(self.cells[i])):
                g_neighbours = self.find_neighbours(i, j)
                if self.cells[i][j] == 0:  # The color of the cell is RED
                    if g_neighbours == 3 or g_neighbours == 6:
                        mutated_matrix[i][j] = 1  # red -> green
                else:  # The color of the cell is GREEN
                    if g_neighbours == 0 or \
                            g_neighbours == 1 or \
                            g_neighbours == 4 or \
                            g_neighbours == 5 or \
                            g_neighbours == 7 or \
                            g_neighbours == 8:
                        mutated_matrix[i][j] = 0  # green -> red

        if mutated_matrix[searched_row][searched_col] == 1:
            square.generations += 1
        """"=============================================="""
        """"       Returning the matrix after the 
              new values have been assigned to the object """
        """" ============================================="""
        self.cells = mutated_matrix
        return self.cells

    def iterate_matrix_n_times(self, n, matrix):

        for i in range(n):
            matrix = self.transform_matrix_once()
            # print(matrix)

        return matrix


"""==================================================="""
"""   ****  Reading input from the console   ****     """
"""==================================================="""

dimensions = list(map(int, input().split(", ")))

rows = dimensions[0]
columns = dimensions[1]

""" Switched sides of rows and columns of the searched cell to match 
the requirements of the "Example 1" in the task in order [1,0] to be 
top center cell of 3x3 grid"""

wanted_coordinates_and_generation = list(map(int, input().split(", ")))

searched_row = wanted_coordinates_and_generation[1]
searched_col = wanted_coordinates_and_generation[0]
searched_generations = wanted_coordinates_and_generation[2]

""" Creating object of type Cell """
square = Cell(searched_col, searched_row)

""" Creating Matrix object grid"""
grid = Matrix(rows, columns)

""" Filling the matrix at generation 0"""
grid.default_matrix_filling(square)

# grid.draw_matrix()        # Prints the matrix
# print(grid.transform_matrix_once())  # Prints the matrix after one transformation

"""================================"""
"""     Rotates matrix N times     """
"""================================"""

final_matrix = grid.iterate_matrix_n_times(searched_generations, grid.cells)

print(f"Cell [{searched_col},{searched_row}] has been green {square.generations} times")
