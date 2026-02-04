"""
Game state - pure game logic, no rendering.
"""

import random
from src.geo_utils import move_position, distance_meters
from src.config import (
    PLAYER_SPEED_MPS,
    MAP_BOUNDS,
    FLAG_COUNT,
    FLAG_CAPTURE_RADIUS_METERS,
    FLAG_CAPTURE_TIME_SECONDS,
    FLAG_MIN_SPACING_METERS,
)


class Flag:
    """A capturable flag on the map."""

    def __init__(self, lat: float, lng: float):
        self.lat = lat
        self.lng = lng
        self.owner: int | None = None  # None = neutral, 1 = player 1, etc.
        self.capture_progress: float = 0.0  # 0.0 to 1.0
        self.being_captured_by: "Player | None" = None

    def reset_capture(self) -> None:
        """Reset capture progress."""
        self.capture_progress = 0.0
        self.being_captured_by = None


class Player:
    """A player on the map."""

    def __init__(self, lat: float, lng: float, team: int = 1):
        self.lat = lat
        self.lng = lng
        self.team = team
        self.heading = 0.0  # degrees: 0=North, 90=East, 180=South, 270=West
        self.speed = PLAYER_SPEED_MPS
        self.is_capturing: bool = False
        self.capture_target: Flag | None = None

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
        # Start players at opposite corners of map
        lat_offset = (MAP_BOUNDS["max_lat"] - MAP_BOUNDS["min_lat"]) * 0.2
        lng_offset = (MAP_BOUNDS["max_lng"] - MAP_BOUNDS["min_lng"]) * 0.2

        # Player 1 (blue) starts bottom-left
        p1_lat = MAP_BOUNDS["min_lat"] + lat_offset
        p1_lng = MAP_BOUNDS["min_lng"] + lng_offset
        self.player1 = Player(p1_lat, p1_lng, team=1)

        # Player 2 (red) starts top-right
        p2_lat = MAP_BOUNDS["max_lat"] - lat_offset
        p2_lng = MAP_BOUNDS["max_lng"] - lng_offset
        self.player2 = Player(p2_lat, p2_lng, team=2)

        # Keep .player alias for backwards compatibility
        self.player = self.player1

        self.flags: list[Flag] = []
        self._place_flags()

    def _place_flags(self) -> None:
        """Place flags randomly with minimum spacing."""
        max_attempts = 100

        while len(self.flags) < FLAG_COUNT:
            # Random position within map bounds
            lat = random.uniform(MAP_BOUNDS["min_lat"], MAP_BOUNDS["max_lat"])
            lng = random.uniform(MAP_BOUNDS["min_lng"], MAP_BOUNDS["max_lng"])

            # Check distance from all existing flags
            valid = True
            for existing_flag in self.flags:
                dist = distance_meters(lat, lng, existing_flag.lat, existing_flag.lng)
                if dist < FLAG_MIN_SPACING_METERS:
                    valid = False
                    break

            if valid:
                self.flags.append(Flag(lat, lng))
            else:
                max_attempts -= 1
                if max_attempts <= 0:
                    # Could not place all flags with spacing, use what we have
                    break

    def _check_player_capture(self, player: Player, dt: float) -> None:
        """Check if a player is within capture radius of any flag and update capture progress."""
        # Find the closest uncaptured or enemy flag in range
        closest_flag: Flag | None = None
        closest_distance = float("inf")

        for flag in self.flags:
            # Skip flags already owned by this player
            if flag.owner == player.team:
                continue

            dist = distance_meters(player.lat, player.lng, flag.lat, flag.lng)
            if dist <= FLAG_CAPTURE_RADIUS_METERS and dist < closest_distance:
                closest_distance = dist
                closest_flag = flag

        # Handle capture logic
        if closest_flag is not None:
            # Check if another player is already capturing this flag
            if closest_flag.being_captured_by is not None and closest_flag.being_captured_by != player:
                # Contested! Reset progress and neither can capture
                closest_flag.reset_capture()
                player.is_capturing = False
                player.capture_target = None
                return

            # Player is in range of a capturable flag
            if player.capture_target != closest_flag:
                # Started capturing a new flag, reset progress
                if player.capture_target is not None:
                    player.capture_target.reset_capture()
                player.is_capturing = True
                player.capture_target = closest_flag
                closest_flag.being_captured_by = player
                closest_flag.capture_progress = 0.0

            # Update capture progress
            closest_flag.capture_progress += dt / FLAG_CAPTURE_TIME_SECONDS

            if closest_flag.capture_progress >= 1.0:
                # Capture complete!
                closest_flag.owner = player.team
                closest_flag.capture_progress = 1.0
                closest_flag.being_captured_by = None
                player.is_capturing = False
                player.capture_target = None
        else:
            # Player left capture radius - reset capture
            if player.is_capturing and player.capture_target is not None:
                player.capture_target.reset_capture()
            player.is_capturing = False
            player.capture_target = None

    def _check_flag_captures(self, dt: float) -> None:
        """Check flag captures for all players."""
        self._check_player_capture(self.player1, dt)
        self._check_player_capture(self.player2, dt)

    def update(self, dt: float, p1_directions: list[str], p2_directions: list[str]) -> None:
        """
        Update game state.

        Args:
            dt: Delta time in seconds
            p1_directions: List of active directions for player 1 (arrow keys)
            p2_directions: List of active directions for player 2 (WASD)
        """
        for direction in p1_directions:
            self.player1.move(direction, dt)

        for direction in p2_directions:
            self.player2.move(direction, dt)

        self._check_flag_captures(dt)
