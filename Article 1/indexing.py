from manim import *
from matrix import MyMatrix


class RowMajor(Scene):
    def construct(self):
        m0 = MyMatrix(rows=3, columns=3)
        m1 = MyMatrix(rows=1, columns=9)
        self.add(m0)
        self.wait()
        self.play(Transform(m0, m1), run_time=2)
        self.wait()