"""Configuration settings for a first Prototype with a  Static map with single movable player"""

MAP_IMAGE_PATH = "assets/map.png"
MAP_BOUNDS = {
    "min_lat": 47.43931,
    "max_lat": 47.46416,
    "min_lng": 8.12919,
    "max_lng": 8.18584
}
MAP_SIZE_PIXELS = (1925, 1248)  # of your PNG

# Player settings
PLAYER_SPEED_MPS = 7  # meters per second ≈ 25 km/h
PLAYER_COLOR = (0, 100, 255)  # Blue
