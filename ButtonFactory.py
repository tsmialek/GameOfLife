from abc import ABC, abstractmethod
import pygame
import numpy as np
import os

# Button contract
class Button(ABC):
    def __init__(self, x, y, width, height):
       self.rect = pygame.Rect(x, y, width, height)
       self.width = width
       self.height = height
       self.x = x
       self.y = y

    def draw(self, screen, color, text, text_color):
        pygame.draw.rect(screen, color, self.rect)
        font = pygame.font.Font(None, 24)
        text = font.render(text, True, text_color)
        text_rect = text.get_rect(center=(self.rect.x + self.width // 2, self.rect.y + self.height // 2))
        screen.blit(text, text_rect)

    @abstractmethod
    def click_logic(self):
        pass

    def click_detection(self, event) -> bool:
        if (
            event.type == pygame.MOUSEBUTTONDOWN and
            self.x <= event.pos[0] <= self.x + self.width and
            self.y <= event.pos[1] <= self.y + self.height
        ):
            return True
        return False

# Concrete products
class NextGenerationButton(Button):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def click_logic(self, n_cells_x, n_cells_y, game_state):
        new_state = np.copy(game_state)

        for y in range(n_cells_y):
            for x in range(n_cells_x):
                n_neighbors = game_state[(x - 1) % n_cells_x, (y - 1) % n_cells_y] + \
                            game_state[(x)     % n_cells_x, (y - 1) % n_cells_y] + \
                            game_state[(x + 1) % n_cells_x, (y - 1) % n_cells_y] + \
                            game_state[(x - 1) % n_cells_x, (y)     % n_cells_y] + \
                            game_state[(x + 1) % n_cells_x, (y)     % n_cells_y] + \
                            game_state[(x - 1) % n_cells_x, (y + 1) % n_cells_y] + \
                            game_state[(x)     % n_cells_x, (y + 1) % n_cells_y] + \
                            game_state[(x + 1) % n_cells_x, (y + 1) % n_cells_y]

                if game_state[x, y] == 1 and (n_neighbors < 2 or n_neighbors > 3):
                    new_state[x, y] = 0
                elif game_state[x, y] == 0 and n_neighbors == 3:
                    new_state[x, y] = 1

        return new_state


class SaveButton(Button):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def click_logic(self, game_state):
        # Creating string representation of game state
        game_state_string = self.game_state_to_string(game_state)

        # Save game state to file
        self.save_game_state_to_file(game_state_string)

    def game_state_to_string(self, game_state):
        return '\n'.join(''.join(str(cell) for cell in row) for row in game_state)

    def save_game_state_to_file(self, game_state_string, filename="saved_game.txt"):
        # Getting path to game directory
        game_dir = os.path.dirname(os.path.realpath(__file__))
        # Full path to file
        filepath = os.path.join(game_dir, filename)

        with open(filepath, "w") as file:
            file.write(game_state_string)

        print(f"Game state saved to {filepath}")
    

class LoadButton(Button):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def click_logic(self, filename="saved_game.txt"):
        # Getting path to game directory
        game_dir = os.path.dirname(os.path.realpath(__file__))
        # Full path to file
        filepath = os.path.join(game_dir, filename)
        try:
            with open(filepath, "r") as file:
                game_state_string = file.read()
            print(f"Game state loaded from {filepath}")
            return self.string_to_game_state(game_state_string)
        except IOError:
            print(f"Could not load game from {filepath}")
            return None

    def string_to_game_state(self, game_state_string):
        game_state_rows = game_state_string.strip().split('\n')
        game_state = np.array([list(map(int, row)) for row in game_state_rows])
        return game_state


class AutomaticGenButton(NextGenerationButton):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    

class PauseButton(Button):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def click_logic(self):
        # ToDo:
        pass

class ExitButton(Button):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def click_logic(self):
        print("Thanks for playing!")
        pygame.quit()

# ---------------------------------------------------------------

class ButtonFactory():
    def create_button(self, type, x, y, width = 200, height = 50):
        if type == "next_generation":
            return NextGenerationButton(x, y, width, height)
        elif type == "save":
            return SaveButton(x, y, width, height)
        elif type == "load":
            return LoadButton(x, y, width, height)
        elif type == "automatic_gen":
            return AutomaticGenButton(x, y, width, height)
        elif type == "exit":
            return ExitButton(x, y, width, height)
        elif type == "pause":
            return PauseButton(x, y, width, height)
        else:
            raise ValueError("Unknown button type")

