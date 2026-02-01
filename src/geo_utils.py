"""
Geo utilities for converting between coordinates and pixels.
Uses geopy for distance and destination calculations.
"""

from geopy.distance import geodesic # type: ignore[import-untyped]
from geopy import Point # type: ignore[import-untyped]

from src.config import MAP_BOUNDS, MAP_SIZE_PIXELS


def distance_meters(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    """Calculate distance in meters between two lat/lng points."""
    return geodesic((lat1, lng1), (lat2, lng2)).meters


def move_position(lat: float, lng: float, heading: float, distance_m: float) -> tuple[float, float]:
    """
    Move from a position in a given direction.

    Args:
        lat, lng: Starting position
        heading: Direction in degrees (0=North, 90=East, 180=South, 270=West)
        distance_m: Distance to move in meters

    Returns:
        (new_lat, new_lng)
    """
    start = Point(lat, lng)
    destination = geodesic(meters=distance_m).destination(start, bearing=heading)
    return destination.latitude, destination.longitude


def latlng_to_pixel(lat: float, lng: float) -> tuple[int, int]:
    """
    Convert lat/lng to pixel position on the map image.

    Longitude → X (left to right)
    Latitude → Y (inverted: top is max_lat, bottom is min_lat)
    """
    min_lat, max_lat = MAP_BOUNDS["min_lat"], MAP_BOUNDS["max_lat"]
    min_lng, max_lng = MAP_BOUNDS["min_lng"], MAP_BOUNDS["max_lng"]
    width, height = MAP_SIZE_PIXELS

    x = (lng - min_lng) / (max_lng - min_lng) * width
    y = (max_lat - lat) / (max_lat - min_lat) * height

    return int(x), int(y)


def pixel_to_latlng(x: int, y: int) -> tuple[float, float]:
    """Convert pixel position to lat/lng coordinates."""
    min_lat, max_lat = MAP_BOUNDS["min_lat"], MAP_BOUNDS["max_lat"]
    min_lng, max_lng = MAP_BOUNDS["min_lng"], MAP_BOUNDS["max_lng"]
    width, height = MAP_SIZE_PIXELS

    lng = min_lng + (x / width) * (max_lng - min_lng)
    lat = max_lat - (y / height) * (max_lat - min_lat)

    return lat, lng


if __name__ == "__main__":
    # Quick tests
    zurich = (47.3779, 8.5403)
    bern = (46.9490, 7.4385)
    print(f"Zurich to Bern: {distance_meters(*zurich, *bern)/1000:.1f} km")

    # Move 1000m north
    new_pos = move_position(47.45, 8.15, heading=0, distance_m=1000)
    print(f"1000m north of (47.45, 8.15): ({new_pos[0]:.5f}, {new_pos[1]:.5f})")

    # Pixel round-trip
    center = ((MAP_BOUNDS["min_lat"] + MAP_BOUNDS["max_lat"]) / 2,
              (MAP_BOUNDS["min_lng"] + MAP_BOUNDS["max_lng"]) / 2)
    px = latlng_to_pixel(*center)
    back = pixel_to_latlng(*px)
    print(f"Center {center} -> pixel {px} -> back {back}")
