from functools import partial

import numpy
from manim import *


def new_index(index, rows, columns):
    if index == rows * columns - 1:
        return index
    return (columns * index) % (rows * columns - 1)


def search_cycle(index, rows, columns):
    new = partial(new_index, rows=rows, columns=columns)
    cycle = [index]
    current = index
    while True:
        next_item = new(current)
        if next_item == cycle[0]:
            return cycle
        cycle.append(next_item)
        current = next_item


def make_cycles(rows, columns):
    visited = [False] * (rows * columns)
    cycles = []
    for i in range(rows * columns):
        if visited[i]:
            continue
        cycle = search_cycle(i, rows, columns)
        cycles.append(cycle)
        for j in cycle:
            visited[j] = True
    return cycles


class Confusing(Scene):
    def construct(self):
        rows, columns = 4, 2
        reference_matrix = Matrix(
            [
                numpy.array(
                    [[row * columns + i for i in range(columns)] for row in range(rows)]
                ).T.flatten()
            ]
        ).shift(DOWN / 2)
        m_objects = [Integer(number=i) for i in range(rows * columns)]
        matrix = MobjectMatrix([m_objects]).shift(UP / 2)
        self.add(reference_matrix)
        self.add(matrix)
        self.wait()

        cycles = make_cycles(rows, columns)
        cyclic_replacements = []
        for cycle in cycles:
            if len(cycle) > 1:
                # reversing this because manim puts the last element first
                m_object_cycle = [m_objects[i] for i in cycle[::-1]]
                cyclic_replacements.append(CyclicReplace(*m_object_cycle))

        self.play(*cyclic_replacements)
        self.wait()

        self.play(
            reference_matrix.animate.shift(UP / 2),
            matrix.animate.shift(DOWN / 2),
        )
        self.play(
            reference_matrix.animate.fade(1),
            Create(SurroundingRectangle(matrix.get_rows()[0])),
        )
        self.remove(reference_matrix)
        self.wait()
