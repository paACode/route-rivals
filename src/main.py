"""
Main entry point - game loop and input handling.
"""

import pygame

from src.game_state import GameState
from src.renderer import Renderer


def main() -> None:
    game_state = GameState()
    renderer = Renderer()
    clock = pygame.time.Clock()

    running = True
    while running:
        # Delta time in seconds
        dt = clock.tick(60) / 1000.0

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Get pressed keys for continuous movement
        keys = pygame.key.get_pressed()

        # Player 1: Arrow keys
        p1_directions = []
        if keys[pygame.K_UP]:
            p1_directions.append("north")
        if keys[pygame.K_DOWN]:
            p1_directions.append("south")
        if keys[pygame.K_LEFT]:
            p1_directions.append("west")
        if keys[pygame.K_RIGHT]:
            p1_directions.append("east")

        # Player 2: WASD
        p2_directions = []
        if keys[pygame.K_w]:
            p2_directions.append("north")
        if keys[pygame.K_s]:
            p2_directions.append("south")
        if keys[pygame.K_a]:
            p2_directions.append("west")
        if keys[pygame.K_d]:
            p2_directions.append("east")

        # Update game state
        game_state.update(dt, p1_directions, p2_directions)

        # Render
        renderer.draw(game_state)
        pygame.display.flip()

    renderer.quit()


if __name__ == "__main__":
    main()
