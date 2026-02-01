"""
Renderer - handles all pygame drawing.
"""

import pygame

from src.config import MAP_IMAGE_PATH, MAP_SIZE_PIXELS, PLAYER_COLOR
from src.geo_utils import latlng_to_pixel
from src.game_state import GameState


class Renderer:
    """Handles all rendering to the screen."""

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(MAP_SIZE_PIXELS)
        pygame.display.set_caption("RouteRivals Prototype")

        # Load map image
        self.map_image = pygame.image.load(MAP_IMAGE_PATH).convert()

        # Player settings
        self.player_radius = 10

        # Font for debug info
        self.font = pygame.font.Font(None, 24)

    def draw(self, game_state: GameState) -> None:
        """Draw the current game state."""
        # Draw map background
        self.screen.blit(self.map_image, (0, 0))

        # Draw player
        player = game_state.player
        px, py = latlng_to_pixel(player.lat, player.lng)
        pygame.draw.circle(self.screen, PLAYER_COLOR, (px, py), self.player_radius)

        # Draw debug info
        debug_text = f"Lat: {player.lat:.5f}  Lng: {player.lng:.5f}"
        text_surface = self.font.render(debug_text, True, (255, 255, 255))
        # Draw with black background for readability
        text_bg = pygame.Surface((text_surface.get_width() + 10, text_surface.get_height() + 6))
        text_bg.fill((0, 0, 0))
        text_bg.set_alpha(180)
        self.screen.blit(text_bg, (5, 5))
        self.screen.blit(text_surface, (10, 8))

    def quit(self) -> None:
        """Clean up pygame."""
        pygame.quit()
