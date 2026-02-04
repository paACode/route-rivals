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
PLAYER_SPEED_MPS = 139  # meters per second ≈ 1000 km/h
PLAYER_1_COLOR = (0, 100, 255)  # Blue
PLAYER_COLOR = PLAYER_1_COLOR  # Alias for backwards compatibility

# Flag settings
FLAG_COUNT = 10
FLAG_CAPTURE_RADIUS_METERS = 75
FLAG_CAPTURE_TIME_SECONDS = 10
FLAG_MIN_SPACING_METERS = 400
FLAG_COLOR_NEUTRAL = (200, 200, 200)
FLAG_COLOR_PLAYER_1 = (0, 100, 255)  # Blue
