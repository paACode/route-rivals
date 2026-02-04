"""
Renderer - handles all pygame drawing.
"""

import pygame

import math
from src.config import (
    MAP_IMAGE_PATH,
    MAP_SIZE_PIXELS,
    PLAYER_1_COLOR,
    PLAYER_2_COLOR,
    FLAG_COLOR_NEUTRAL,
    FLAG_COLOR_PLAYER_1,
    FLAG_COLOR_PLAYER_2,
    FLAG_CAPTURE_RADIUS_METERS,
)
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
        self.player_radius = 8

        # Flag settings
        self.flag_radius = 12
        # Approximate pixels per meter (based on map scale)
        # Map is roughly 5km wide, so 5000m / 1925px ≈ 2.6m per pixel
        self.meters_per_pixel = 5000 / MAP_SIZE_PIXELS[0]
        self.capture_radius_pixels = int(FLAG_CAPTURE_RADIUS_METERS / self.meters_per_pixel)

        # Font for debug info
        self.font = pygame.font.Font(None, 24)

    def _draw_flags(self, game_state: GameState) -> None:
        """Draw all flags and their capture progress."""
        for flag in game_state.flags:
            fx, fy = latlng_to_pixel(flag.lat, flag.lng)

            # Determine flag color based on owner
            if flag.owner is None:
                color = FLAG_COLOR_NEUTRAL
            elif flag.owner == 1:
                color = FLAG_COLOR_PLAYER_1
            elif flag.owner == 2:
                color = FLAG_COLOR_PLAYER_2
            else:
                color = FLAG_COLOR_NEUTRAL

            # Draw capture radius circle (semi-transparent)
            radius_surface = pygame.Surface(
                (self.capture_radius_pixels * 2, self.capture_radius_pixels * 2),
                pygame.SRCALPHA
            )
            pygame.draw.circle(
                radius_surface,
                (*color, 40),  # Semi-transparent
                (self.capture_radius_pixels, self.capture_radius_pixels),
                self.capture_radius_pixels
            )
            self.screen.blit(
                radius_surface,
                (fx - self.capture_radius_pixels, fy - self.capture_radius_pixels)
            )

            # Draw the flag itself
            pygame.draw.circle(self.screen, color, (fx, fy), self.flag_radius)
            pygame.draw.circle(self.screen, (0, 0, 0), (fx, fy), self.flag_radius, 2)

            # Draw capture progress arc if being captured
            if flag.being_captured_by is not None and flag.capture_progress > 0:
                self._draw_capture_progress(fx, fy, flag.capture_progress)

    def _draw_capture_progress(self, x: int, y: int, progress: float) -> None:
        """Draw a progress arc around the flag."""
        arc_radius = self.flag_radius + 6
        arc_width = 4
        # Green progress arc
        arc_color = (50, 200, 50)

        # Draw arc from top (270 degrees in pygame) clockwise
        start_angle = math.pi / 2  # Top
        end_angle = start_angle - (progress * 2 * math.pi)

        rect = pygame.Rect(x - arc_radius, y - arc_radius, arc_radius * 2, arc_radius * 2)
        pygame.draw.arc(self.screen, arc_color, rect, end_angle, start_angle, arc_width)

    def draw(self, game_state: GameState) -> None:
        """Draw the current game state."""
        # Draw map background
        self.screen.blit(self.map_image, (0, 0))

        # Draw flags first (below players)
        self._draw_flags(game_state)

        # Draw player 1 (blue)
        p1 = game_state.player1
        p1x, p1y = latlng_to_pixel(p1.lat, p1.lng)
        pygame.draw.circle(self.screen, PLAYER_1_COLOR, (p1x, p1y), self.player_radius)
        pygame.draw.circle(self.screen, (255, 255, 255), (p1x, p1y), self.player_radius, 2)

        # Draw player 2 (red)
        p2 = game_state.player2
        p2x, p2y = latlng_to_pixel(p2.lat, p2.lng)
        pygame.draw.circle(self.screen, PLAYER_2_COLOR, (p2x, p2y), self.player_radius)
        pygame.draw.circle(self.screen, (255, 255, 255), (p2x, p2y), self.player_radius, 2)

        # Count captured flags for each team
        p1_flags = sum(1 for f in game_state.flags if f.owner == 1)
        p2_flags = sum(1 for f in game_state.flags if f.owner == 2)
        total_flags = len(game_state.flags)

        # Build score display
        score_text = f"Blue: {p1_flags}  Red: {p2_flags}  (of {total_flags})"

        # Show capture progress if either player is capturing
        capture_info = ""
        if p1.is_capturing and p1.capture_target:
            progress_pct = int(p1.capture_target.capture_progress * 100)
            capture_info += f"  [Blue capturing: {progress_pct}%]"
        if p2.is_capturing and p2.capture_target:
            progress_pct = int(p2.capture_target.capture_progress * 100)
            capture_info += f"  [Red capturing: {progress_pct}%]"

        debug_text = score_text + capture_info

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
