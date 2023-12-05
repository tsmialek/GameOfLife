import pygame 
import numpy as np
import PygameSinglegon
import CellFactory
import ButtonFactory

class GameRenderer:
    def __init__(self, pgs, cell_factory, button_factory):
        self.pgs = pgs
        self.cell_factory = cell_factory
        self.button_factory = button_factory

    def draw_grid(self):
        gray = (128, 128, 128)
        cell_width, cell_height = self.pgs.get_cell_dimensions()
        height, width = self.pgs.get_height_abs(), self.pgs.get_width()

        for y in range(0, height - self.pgs.button_bar_height, cell_height):
            for x in range(0, width, cell_width):
                pygame.draw.rect(self.pgs.get_screen(), gray, (x, y, cell_width, cell_height), 1)

    def draw_cells(self, game_state):
        n_cells_x, n_cells_y = self.pgs.get_cell_number()
        cell_width, cell_height = self.pgs.get_cell_dimensions()

        for y in range(n_cells_y):
            for x in range(n_cells_x):
                alive_cell = self.cell_factory.create_cell(x, y, cell_width, cell_height, 'alive')
                if game_state[x, y] == 1:
                    alive_cell.draw(self.pgs.get_screen())

    def draw_button(self, type, text, color, x, y, width = 200, height = 50):
        screen = self.pgs.get_screen()
        button = self.button_factory.create_button(type, x, y, width, height)
        button.draw(self.pgs.get_screen(), color, text, (255, 255, 255))
        return button
                                            
        

# ToDo:
# next generation
# drawing buttons