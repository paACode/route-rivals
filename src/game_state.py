"""
Game state - pure game logic, no rendering.
"""

from src.geo_utils import move_position
from src.config import PLAYER_SPEED_MPS, MAP_BOUNDS


class Player:
    """A player on the map."""

    def __init__(self, lat: float, lng: float, team: int = 1):
        self.lat = lat
        self.lng = lng
        self.team = team
        self.heading = 0.0  # degrees: 0=North, 90=East, 180=South, 270=West
        self.speed = PLAYER_SPEED_MPS

    def move(self, direction: str, dt: float) -> None:
        """
        Move the player in a cardinal direction.

        Args:
            direction: "north", "south", "east", or "west"
            dt: Delta time in seconds
        """
        headings = {
            "north": 0,
            "east": 90,
            "south": 180,
            "west": 270,
        }

        if direction not in headings:
            return

        self.heading = headings[direction]
        distance = self.speed * dt

        new_lat, new_lng = move_position(self.lat, self.lng, self.heading, distance)

        # Clamp to map bounds
        new_lat = max(MAP_BOUNDS["min_lat"], min(MAP_BOUNDS["max_lat"], new_lat))
        new_lng = max(MAP_BOUNDS["min_lng"], min(MAP_BOUNDS["max_lng"], new_lng))

        self.lat = new_lat
        self.lng = new_lng


class GameState:
    """Manages all game objects and logic."""

    def __init__(self):
        # Start player at center of map
        center_lat = (MAP_BOUNDS["min_lat"] + MAP_BOUNDS["max_lat"]) / 2
        center_lng = (MAP_BOUNDS["min_lng"] + MAP_BOUNDS["max_lng"]) / 2

        self.player = Player(center_lat, center_lng, team=1)

    def update(self, dt: float, directions: list[str]) -> None:
        """
        Update game state.

        Args:
            dt: Delta time in seconds
            directions: List of active directions ("north", "south", "east", "west")
        """
        for direction in directions:
            self.player.move(direction, dt)
