import pygame
import numpy as np

class PygameSingleton:
    _instance = None

    def __new__ (
            cls, 
            width = 800, height = 600, 
            n_cells_x = 40, n_cells_y = 30, 
            p = [0.8, 0.2],
            button_bar_height = 60
    ):
        if not cls._instance: 
            cls._instance = super(PygameSingleton, cls).__new__(cls)
            cls._instance.initialize(width, height)

        return cls._instance

    def initialize(
            self, 
            width = 800, height = 600, 
            n_cells_x = 40, n_cells_y = 30, 
            p = [0.8, 0.2],
            button_bar_height = 50
    ):
    # Initialize Pygame
        pygame.init()
    # Screen dimensions
        self.width = width
        self.height = height
        self.height_absolute = height + button_bar_height
        self.button_bar_height = button_bar_height
        self.screen = pygame.display.set_mode((width, self.height_absolute))
    # Cell dimensions 
        self.cell_height = height // n_cells_y
        self.cell_width = width // n_cells_x
        self.n_cells_x = n_cells_x
        self.n_cells_y = n_cells_y
    # Game state
        self.game_state = np.random.choice([0, 1], size=(n_cells_x, n_cells_y), p=p)
    
    # Get methods
    def get_screen(self):
        return self.screen 
    
    def get_cell_dimensions(self):
        return self.cell_width, self.cell_height

    def get_cell_number(self):
        return self.n_cells_x, self.n_cells_y   

    def get_game_state(self):
        return self.game_state
    
    def get_width(self):
        return self.width
    
    def get_height(self):    
        return self.height

    def get_height_abs(self):    
        return self.height_absolute