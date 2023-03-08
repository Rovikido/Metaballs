from math import ceil
from tkinter import *
from tkinter import Tk



class Cell:
    def __init__(self, center, corners):
        self.center = center
        self.corners = corners

    def add_polygon(self, polygon_data):
        self.polygon_data = polygon_data


class MarchingSquares:
    def __init__(self, gui):
        self.canvas_height = gui.canvas_height
        self.canvas_width = gui.canvas_width
        self.lookup_table = self.gen_lookup_table

    def gen_lookup_table(self):
        table = {}
        table[[False, False, False, False, False]] = [[False, False, False],
                                                      [False, False, False],
                                                      [False, False, False]]
        table[[True, False, False, False, False]] = table[[False, False, False, False, False]]

        table[[True, True, True, True, True]] = [[True, True, True],
                                                 [True, True, True],
                                                 [True, True, True]]
        table[[False, True, True, True, True]] = table[[True, True, True, True, True]]



        table[[False, True, False, False, False]] = [[True, True, False],
                                                     [True, False, False],
                                                     [False, False, False]]
        table[[True, True, False, False, False]] = table[[False, True, False, False, False]]

        table[[False, False, True, False, False]] = [[False, True, True],
                                                     [False, False, True],
                                                     [False, False, False]]
        table[[True, False, True, False, False]] = table[[False, False, True, False, False]]

        table[[False, False, False, True, False]] = [[False, False, False],
                                                     [True, False, False],
                                                     [True, True, False]]
        table[[True, False, False, True, False]] = table[[True, False, False, True, False]]

        table[[False, False, False, False, True]] = [[False, False, False],
                                                     [False, False, True],
                                                     [False, True, True]]
        table[[True, False, False, False, True]] = table[[False, False, False, False, True]]



        table[[False, True, True, False, False]] = [[True, True, True],
                                                    [True, False, True],
                                                    [False, False, False]]
        table[[True, False, False, False, False]] = table[[False, False, False, False, False]]





    def divide_into_grid(self, box_size):
        cell_list = []
        for x in range(0, ceil(self.canvas_height / box_size)):
            for y in range(0, ceil(self.canvas_width / box_size)):
                center = ((x * box_size) + box_size/2, (y * box_size) + box_size/2)
                corners = ((x * box_size, y * box_size),
                           (x * box_size + box_size, y * box_size),
                           (x * box_size, y * box_size + box_size),
                           (x * box_size + box_size, y * box_size + box_size))
                cell_list.append(Cell(center, corners))
        return cell_list

    def compute(self, func, thread_count=10, box_size=10, more_than_value=1):
        #TODO: implement threads
        cell_list = self.divide_into_grid(box_size)
        for cell in cell_list:
            self.__compute_cells(cell, func, more_than_value)

    def __compute_cells(self, cell: Cell, func, more_than_value):
        values = [func(cell.center[0], cell.center[1])]
        for cord in cell.corners:
            values.append(func(cord[0], cord[1]))
        states = list(map(lambda x: x >= more_than_value, values))
        #use dictionary with states as lookup values, dict should return activity states for every side and corner






