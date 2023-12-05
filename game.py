# To create & start using python venv:
#       python -m venv venv
#       source venv/bin/activate

# Install specific modules with pip:
# f.e.:   pip install pygame

# Requirements
# 1. Make simulation real time
# 2. Add pause / resume logic
# 3. Add save / load logic

# High-level logic
# 1. Create and init the simulation grid
# 2. Start the simulation with a tick interval of <n> seconds
# 3. At each tick:
#   3.1. Update the grid - loop over each element of the board
#   3.2. Render new generation

# General approach
# 1. Plan & write down the general workflow
#  1.1. Define Input&Output 
#  1.2. Consider adding validation
# 2. Separate the main algorithms / actors in the code. Try to abstract as much common code as possible
# 3. Define communication between the objects
# 4. List the patterns you could apply
# 5. Build PoCs (Proof of concepts). Try to separate implementation of specific steps. Prepare smaller modules
#    and combine them into a complete application
# 6. Refine if needed

# Deadline - 15th of December 2023
# Mail with: 
# 1. short screen recording demonstrating the new features
# 2. Linked code
# 3. Short description of the changes. Which design patterns you used and how you applied them. 

import pygame
import numpy as np
from PygameSinglegon import PygameSingleton
from CellFactory import *
from ButtonFactory import *
from GameRenderer import GameRenderer
import time

# Initialize Pygame
pgs = PygameSingleton()
button_factory = ButtonFactory()
cell_factory = CellFactory()
game_renderer = GameRenderer(pgs, cell_factory, button_factory)

# screen and game state
screen = pgs.get_screen()
game_state = pgs.get_game_state()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
green = (25, 79, 70)
blue = (26, 39, 92)

# button dimensions
button_width, button_height = 800/6, 50
button_y = pgs.get_height_abs() - button_height

# number of cells
n_cells_x, n_cells_y = pgs.get_cell_number()

# time setup 
automatic_generation = False
last_generation_time = 0
generation_interval = 1 # seconds

# Main loop
running = True
while running:
    current_time = time.time()
    screen.fill(white)
    game_renderer.draw_grid()

    # draw buttons
    next_generation_button = game_renderer.draw_button('next_generation', 'Next Generation', blue, 0, button_y, button_width, button_height)
    save_button = game_renderer.draw_button('save', 'Save', green, button_width, button_y, button_width, button_height)
    load_button = game_renderer.draw_button('load', 'Load', blue, 2 * button_width, button_y, button_width, button_height)
    automatic_gen_button = game_renderer.draw_button('automatic_gen', 'Start generation', green, 3 * button_width, button_y, button_width, button_height)
    pause_button = game_renderer.draw_button('pause', 'Pause', blue, 4 * button_width, button_y, button_width, button_height)
    exit_button = game_renderer.draw_button('exit', 'Exit', green, 5 * button_width, button_y, button_width, button_height) 

    # draw cells
    game_renderer.draw_cells(game_state) 

    # checking if automatic generation is on
    if automatic_generation and current_time - last_generation_time > generation_interval:
        game_state = automatic_gen_button.click_logic(n_cells_x, n_cells_y, game_state)
        last_generation_time = current_time

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if next_generation_button.click_detection(event) and not automatic_generation:
                game_state = next_generation_button.click_logic(n_cells_x, n_cells_y, game_state)
            elif exit_button.click_detection(event):
                exit_button.click_logic()
            elif save_button.click_detection(event):
                save_button.click_logic(game_state)
            elif load_button.click_detection(event):
                game_state = load_button.click_logic()
            elif automatic_gen_button.click_detection(event):
                automatic_generation = True
                last_generation_time = current_time
            elif pause_button.click_detection(event):
                automatic_generation = False
            else:
                try:
                    x, y = event.pos[0] // pgs.cell_width, event.pos[1] // pgs.cell_height
                    game_state[x, y] = not game_state[x, y]
                except IndexError:
                    pass

    pygame.display.flip()

pygame.quit()

