from manim import Matrix, Swap
import numpy


class MyMatrix(Matrix):
    def __init__(self, rows, columns):
        self.rows, self.columns = rows, columns
        display_matrix = [[j*columns+i for i in range(columns)] for j in range(rows)]
        super().__init__(display_matrix, left_bracket="[", right_bracket=']')
        # unraveling the display matrix to store internally
        # this numpy matrix is used to apply the transformations because I am not gonna code those by hand lol
        self.matrix = numpy.array([[j*columns + i for i in range(columns)] for j in range(rows)])

    def get_transpose_swaps(self):
        self.rows, self.columns = self.columns, self.rows
        swaps = []
        for i, row in enumerate(self.matrix.T):
            for j, element in enumerate(row):
                og_index = element
                current_index = self.columns * i + j
                swaps.append(Swap(self.elements[og_index], self.elements[current_index]))
        return swaps
