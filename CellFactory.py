from abc import ABC, abstractmethod
import pygame

# Product "interface"
class Cell(ABC):

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x * width, y * height, width, height)

    @abstractmethod
    def draw(self, screen, color):
        pass 

# Concrete product
class AliveCell(Cell):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def draw(self, screen, color = (0, 0, 0)):
        pygame.draw.rect(screen, color, self.rect)

class DeadCell(Cell):
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def draw(self, screen, color = (255, 255, 255)):
        pygame.draw.rect(screen, color, self.rect)
        

# Define the Cell contract
class CellFactory():
    def create_cell(self, x, y, width, height, type): 
        if type == 'alive':
            return AliveCell(x, y, width, height)
        elif type == 'dead':
            return DeadCell(x, y, width, height)
        else:
            raise ValueError('Invalid cell type: ' + type)