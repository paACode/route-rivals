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
        directions = []
        if keys[pygame.K_UP]:
            directions.append("north")
        if keys[pygame.K_DOWN]:
            directions.append("south")
        if keys[pygame.K_LEFT]:
            directions.append("west")
        if keys[pygame.K_RIGHT]:
            directions.append("east")

        # Update game state
        game_state.update(dt, directions)

        # Render
        renderer.draw(game_state)
        pygame.display.flip()

    renderer.quit()


if __name__ == "__main__":
    main()
