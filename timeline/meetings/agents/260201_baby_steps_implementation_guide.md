# RouteRivals Prototype: Baby Steps Implementation Guide

**Date**: 2026-02-01
**Participants**: User, Senior Software Architect, Mobile GPS Gaming Specialist
**Topic**: First implementation steps for desktop prototype

---

## Meeting Summary

Both experts validated the user's proposed approach:
1. Create a simple map with flags
2. Add 1 player controllable with arrow keys
3. Player can capture flags
4. Add second player, see territory turn red
5. Implement first skills
6. Play around with map size

**Consensus**: Desktop-first with Python is the right call. Sequential feature addition allows rapid iteration.

---

## Agreed Technical Stack

- **Pygame** - Rendering and game loop
- **Static OSM image** - Skip tile management for prototype
- **SciPy** - Voronoi territory visualization (later)
- **Pillow** - Image handling

---

## Critical GPS Simulation Requirements

Even on desktop, simulate these constraints or the prototype will give false feedback:

| Constraint | Value | Why |
|------------|-------|-----|
| Position delay | 500-800ms | GPS doesn't update instantly |
| Position jitter | 5-15m random | GPS isn't precise |
| Road-only movement | Snap to roads | Cyclists can't cut fields |
| Speed limits | 15-35 km/h | Cycling physics |

---

## Recommended Map Scale

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Play area | 5km × 5km | Matches 1-2 hour cycling session |
| Flag count | 8-12 | Strategic choices without clutter |
| Flag spacing | 400-600m (road distance) | ~1 minute cycling between flags |
| Capture radius | 75-100m | GPS jitter makes smaller radii frustrating |

---

## Sprint Plan

| Days | Goal | Deliverable |
|------|------|-------------|
| 1-2 | Foundation | Static map + 1 player moving with arrow keys |
| 3 | Flags | 5-10 flags with capture detection |
| 4-5 | Territory | Colored region visualization |
| 6-7 | Multiplayer | Second player (WASD), territory conflict |

**Then STOP and playtest extensively before adding skills.**

---

## Detailed Implementation Guide

### Phase 1: Foundation (Days 1-2)

#### Step 1.1: Project Setup

Create this structure:
```
route-rivals-prototype/
├── main.py              # Entry point, game loop
├── config.py            # All tunable parameters
├── game_state.py        # Pure game logic
├── renderer.py          # Pygame rendering
├── gps_simulator.py     # Simulates GPS behavior
├── geo_utils.py         # Coordinate math
├── assets/
│   └── map.png          # Your exported OSM image
└── requirements.txt
```

**Dependencies**: `pygame`, `scipy`, `pillow`

---

#### Step 1.2: Get Your Map

1. Go to **openstreetmap.org**
2. Navigate to a 5km × 5km area (ideally with good cycling roads)
3. Note the **bounding box coordinates** (visible in URL or export dialog):
   - `min_lat`, `max_lat`, `min_lng`, `max_lng`
4. Export as PNG (or use screenshot at consistent zoom)
5. Save to `assets/map.png`

Store these bounds in `config.py` for pixel-to-coordinate conversion.

---

#### Step 1.3: Config File

Define everything tunable in one place:

```python
# Map settings
MAP_IMAGE_PATH = "assets/map.png"
MAP_BOUNDS = {
    "min_lat": ...,
    "max_lat": ...,
    "min_lng": ...,
    "max_lng": ...
}
MAP_SIZE_PIXELS = (width, height)  # of your PNG

# Player settings
PLAYER_SPEED_MPS = 7  # meters per second ≈ 25 km/h
PLAYER_1_COLOR = (0, 100, 255)  # Blue
PLAYER_2_COLOR = (255, 50, 50)  # Red

# Flag settings
FLAG_COUNT = 10
FLAG_CAPTURE_RADIUS_METERS = 75
FLAG_CAPTURE_TIME_SECONDS = 45
FLAG_MIN_SPACING_METERS = 400
FLAG_COLOR_NEUTRAL = (200, 200, 200)

# GPS simulation
GPS_ENABLED = True
GPS_UPDATE_DELAY_MS = 600
GPS_JITTER_METERS = 10
```

---

#### Step 1.4: Geo Utilities

Implement these helper functions in `geo_utils.py`:

**1. Haversine distance**
- Inputs: `(lat1, lng1, lat2, lng2)`
- Output: distance in meters
- Uses Earth radius = 6,371,000m
- Formula: `2 * R * arcsin(sqrt(sin²(Δlat/2) + cos(lat1) * cos(lat2) * sin²(Δlng/2)))`

**2. Pixel to lat/lng**
- Inputs: `(pixel_x, pixel_y, map_bounds, map_size_pixels)`
- Output: `(lat, lng)`
- Linear interpolation: `lat = max_lat - (pixel_y / height) * (max_lat - min_lat)`
- Note: Y is inverted (pixel 0 = top = max_lat)

**3. Lat/lng to pixel**
- Inverse of above
- `pixel_x = (lng - min_lng) / (max_lng - min_lng) * width`
- `pixel_y = (max_lat - lat) / (max_lat - min_lat) * height`

**4. Move position**
- Inputs: `(lat, lng, heading_degrees, distance_meters)`
- Output: new `(lat, lng)`
- Heading: 0 = North, 90 = East, 180 = South, 270 = West
- Uses spherical geometry (bearing formula)

---

#### Step 1.5: Game State

`game_state.py` should be **pure logic, no Pygame imports**.

**Player class:**
```python
class Player:
    lat: float
    lng: float
    heading: float  # degrees, 0 = North
    speed: float    # current speed in m/s
    team: int       # 1 or 2
    is_capturing: bool
    capture_progress: float  # 0.0 to 1.0
    capture_target: Flag | None
```

**Flag class:**
```python
class Flag:
    lat: float
    lng: float
    owner: int | None  # None, 1, or 2
    capture_progress: float
    being_captured_by: Player | None
```

**GameState class:**
```python
class GameState:
    players: list[Player]
    flags: list[Flag]

    def update(self, dt: float):
        """Advance game by dt seconds"""
        pass

    def check_flag_captures(self):
        """Detect players in flag radius"""
        pass

    def get_territory(self):
        """Return ownership data for rendering"""
        pass
```

---

#### Step 1.6: GPS Simulator

Wraps player input to simulate real GPS behavior.

**Responsibilities:**
- Queue position updates with delay (500-800ms)
- Add random jitter to positions (5-15m in random direction)
- Optionally: enforce road snapping (skip for v1)

**Interface:**
```python
class GPSSimulator:
    def request_move(self, player, direction):
        """Called on keypress, queues movement"""
        pass

    def get_simulated_position(self, player):
        """Returns delayed/jittered position"""
        pass

    def update(self, dt):
        """Process queued updates"""
        pass
```

**Make GPS simulation toggleable** via config for testing.

---

#### Step 1.7: Renderer

`renderer.py` handles all Pygame drawing:

- Load and display map image as background
- Draw players as colored circles at pixel positions
- Draw flags as circles (color based on owner)
- Draw capture progress indicator (arc or filling circle)
- Later: draw territory overlay with transparency

**Key principle**: Renderer only reads from GameState, never modifies it.

---

#### Step 1.8: Main Loop

```python
# main.py structure

def main():
    # 1. Initialize Pygame, load map image
    # 2. Create GameState with 1 player at map center
    # 3. Create GPSSimulator
    # 4. Create Renderer

    running = True
    clock = pygame.time.Clock()

    while running:
        dt = clock.tick(60) / 1000.0  # seconds

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle continuous key input
        keys = pygame.key.get_pressed()
        # Arrow keys → GPSSimulator.request_move()

        # Update
        gps_simulator.update(dt)
        game_state.update(dt)

        # Render
        renderer.draw(game_state)
        pygame.display.flip()

        # Debug output
        print(f"Player: {player.lat:.6f}, {player.lng:.6f}")
```

---

### Phase 2: Flags (Day 3)

#### Step 2.1: Flag Placement

- Randomly place 8-12 flags within map bounds
- Ensure minimum spacing (400-600m between flags using haversine)
- Algorithm: place flag, check distance to all existing flags, retry if too close
- Store in GameState.flags

#### Step 2.2: Capture Detection

In `GameState.update()`:
```
for each player:
    for each flag:
        distance = haversine(player.lat, player.lng, flag.lat, flag.lng)
        if distance <= CAPTURE_RADIUS and flag.owner != player.team:
            if not player.is_capturing:
                start_capture(player, flag)
            else:
                player.capture_progress += dt / CAPTURE_TIME
                if player.capture_progress >= 1.0:
                    flag.owner = player.team
                    reset_capture(player)
```

#### Step 2.3: Capture Interruption

- If player leaves radius: reset `capture_progress` to 0
- If enemy enters radius while capturing: pause or contest (design choice)

---

### Phase 3: Territory (Days 4-5)

#### Step 3.1: Voronoi Calculation

```python
from scipy.spatial import Voronoi

# Get flag positions as points
points = [(flag.lng, flag.lat) for flag in flags]  # Note: x=lng, y=lat

# Calculate Voronoi
vor = Voronoi(points)

# Each region corresponds to a flag
# vor.regions contains vertex indices for each cell
# vor.vertices contains actual coordinates
```

Recalculate when flag ownership changes.

#### Step 3.2: Territory Rendering

- Convert Voronoi vertices to pixel coordinates
- Draw semi-transparent filled polygons:
  - Player 1 territory: blue tint (0, 100, 255, 80)
  - Player 2 territory: red tint (255, 50, 50, 80)
  - Neutral: no overlay
- Use `pygame.Surface` with alpha for transparency

---

### Phase 4: Two Players (Days 6-7)

#### Step 4.1: Input Mapping

```python
# Player 1: Arrow keys
if keys[pygame.K_UP]: move_player(player1, "north")
if keys[pygame.K_DOWN]: move_player(player1, "south")
if keys[pygame.K_LEFT]: move_player(player1, "west")
if keys[pygame.K_RIGHT]: move_player(player1, "east")

# Player 2: WASD
if keys[pygame.K_w]: move_player(player2, "north")
if keys[pygame.K_s]: move_player(player2, "south")
if keys[pygame.K_a]: move_player(player2, "west")
if keys[pygame.K_d]: move_player(player2, "east")
```

#### Step 4.2: Scoring

```python
class GameState:
    score_team1: int = 0
    score_team2: int = 0

    def update(self, dt):
        # Points per second for owned flags
        for flag in self.flags:
            if flag.owner == 1:
                self.score_team1 += dt * POINTS_PER_FLAG_PER_SECOND
            elif flag.owner == 2:
                self.score_team2 += dt * POINTS_PER_FLAG_PER_SECOND
```

Display scores on screen via renderer.

#### Step 4.3: Elimination (Optional)

- Check distance between opposing players
- If within 30m for X consecutive seconds → elimination
- Respawn eliminated player at base (map corner or dedicated spawn point)

---

## Testing Checklist

After each phase, verify:

- [ ] Coordinates display correctly (lat/lng match expected map location)
- [ ] Distance calculations are accurate (place two known points, verify haversine)
- [ ] Movement speed feels like cycling (7 m/s = 25 km/h)
- [ ] GPS jitter is noticeable but not game-breaking
- [ ] Capture radius feels right (not too precise, not too loose)
- [ ] Territory visualization is clear at a glance

---

## Key Validation Scenarios

Once two players are working, test these:

**Scenario A: The Chase**
Player A cycles toward a flag. Player B tries to catch them for elimination. Is the 30m detection range + confirmation window exciting?

**Scenario B: Flag Defense**
Player A captured a flag and leaves. Player B arrives to re-capture. Is 45 seconds too long when vulnerable?

**Scenario C: Strategic Decisions**
With 10 flags on the map, do players face interesting choices about which flag to target?

**Time-to-fun metric**: Within 10 minutes of playtesting, players should experience:
1. A meaningful tactical decision
2. An exciting chase attempt
3. A "close call" moment

---

## Decisions Made

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Coordinate system | Lat/lng internally | Matches real GPS, easy mobile transition |
| Distance units | Meters | Real-world, consistent |
| Speed units | Meters/second | Easy math with dt |
| Capture radius | 75-100m | GPS jitter tolerance |
| Map size | 5km × 5km | 1-2 hour play session |
| GPS delay | 500-800ms | Realistic simulation |
| GPS jitter | 5-15m | Typical GPS accuracy |

---

## Next Steps After Prototype

Once the core loop is validated:
1. Add skills (roadblock, exploration tower)
2. Test with real OSM road data (road snapping)
3. Add audio alerts for cycling safety
4. Consider mobile implementation

---

## Expert Agent IDs (for follow-up)

- Senior Software Architect: `af5a7d9`
- Mobile GPS Gaming Specialist: `ad3a0ea`
