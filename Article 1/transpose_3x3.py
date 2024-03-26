from manim import *
from matrix import MyMatrix


class Transpose(Scene):
    def construct(self):
        matrix = MyMatrix(rows=3, columns=3)
        self.add(matrix)
        self.wait()
        self.play(*matrix.get_transpose_swaps())
        self.wait()
        self.play(matrix.animate.shift(UP))
        self.wait()
        flattened = Matrix([matrix.matrix.T.flatten()]).shift(DOWN)
        self.play(TransformFromCopy(matrix, flattened))
        self.wait()

