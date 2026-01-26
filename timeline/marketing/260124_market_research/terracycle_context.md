# TerraCycle Project Context

## Project Overview
TerraCycle is an innovative GPS-based capture-the-flag game designed specifically for cyclists. It aims to transform cycling from a purely performance-focused activity into an augmented sport that combines physical effort with strategic thinking.

## Core Concept
- **Game Type**: Capture the Flag for cyclists
- **Platform**: Mobile app (Android & iOS initially)
- **Technology**: GPS-based positioning and tracking
- **Minimum Players**: 2v2 (but more fun with larger teams)
- **Goal**: Combine competitive gaming with outdoor cycling

## Key Differentiators

### vs. Zwift
- **TerraCycle**: Real outdoor riding with AR gaming layer
- **Zwift**: Indoor virtual environment, static routes
- **Advantage**: Real exploration, fresh air, strategic territory control

### vs. Strava
- **TerraCycle**: Real-time competitive gameplay
- **Strava**: Post-ride segment competition
- **Advantage**: Live competition, team-based, strategic elements

### vs. Traditional Racing
- **TerraCycle**: Safer, more accessible, strategic depth
- **Traditional**: Dangerous, requires high fitness, limited accessibility
- **Advantage**: Lower barrier to entry, tactical over pure power

## Game Mechanics (Proposed)

### Territory & Flags
- Flags placed throughout a selected region
- Players "capture" flags by reaching them and loading a progress bar
- Captured flags turn team color (blue/red)
- Holding flags generates continuous points
- Strategic decisions: which flags to attack/defend

### Player Actions
- **Capture**: Ride to a flag, load progress bar to claim it
- **Defend**: Protect team flags from opponents
- **Attack**: Intercept opponents attempting to capture
- **Trap**: Set traps on routes to slow opponents
- **Skills**: Various abilities (slows, stops, power-ups)

### Scoring System
- Points for capturing flags
- Continuous points for holding flags
- Bonus points for mini-challenges (sprints, climbs)
- Team reaches target score to win

### Mini-Challenges
- Sprint segments for bonus points
- Fastest rider gets most points
- Adds variety and skill-based rewards

### Respawn Mechanics
- If overtaken by opponent, rider must return to base to "revive"
- Adds strategic risk/reward to captures

## Technical Considerations

### Battery Optimization (Critical)
- Major pain point with navigation apps (Komoot, etc.)
- Minimal map rendering
- Efficient GPS polling
- Background processing optimization
- Low-power mode support

### Map Design
- Minimal visual design to save battery
- Clear team color coding (red/blue zones)
- Flag indicators
- Simple route visualization
- Offline map capability

### Connectivity
- Must work in areas with spotty coverage
- Offline mode for gameplay
- Sync when connection available
- Local P2P options?

## Development Roadmap

### MVP (Minimum Viable Product)
- Simple 2v2 Capture the Flag
- Basic map with flag locations
- Team selection and matchmaking
- Core capture mechanics
- Basic scoring
- Battery-efficient design

### Future Phases
1. **Enhanced Multiplayer**: Lobbies to find local cyclists
2. **Open World**: Persistent world with ongoing battles
3. **World vs. World**: Server-based large-scale competition
4. **Events**: Time-limited special game modes
5. **Progression**: Player levels, unlocks, achievements
6. **Social Features**: Clubs, friends, chat

## Target Audience

### Primary
- **Cycling Enthusiasts** who want more engaging group rides
- **Zwift Users** looking for outdoor alternatives
- **Gamers who Cycle** wanting competitive outdoor gaming
- **Social Riders** seeking structured group activities

### Secondary
- Casual cyclists wanting motivation
- Competitive riders seeking training variety
- E-bike riders (accessibility)
- Adventure/gravel cyclists (exploration element)

## Market Opportunity

### Pain Points Addressed
1. **Lack of outdoor Zwift alternative**: No engaging outdoor multiplayer
2. **Racing too serious/dangerous**: Lower-stress competition
3. **Strava too asynchronous**: Real-time competition desired
4. **Solo riding boring**: Gamification adds engagement
5. **Friends in different locations**: Can compete when together

### Unique Value Propositions
- **Real-world augmented sport**: Combines physical and strategic competition
- **Accessible competition**: Don't need to be pro level
- **Exploration incentive**: Discover new routes via flags
- **Strategy over pure power**: Tactical decisions matter
- **Social outdoor experience**: Structured group activities

## Marketing Angles

### Key Messages
1. "Zwift for the real world"
2. "Where cycling meets strategy"
3. "Ride together, compete together"
4. "Explore while you compete"
5. "It's not just about watts"

### Content Ideas
- Demo videos of actual gameplay
- Strategy guides (team compositions, flag priorities)
- Community success stories
- Map/region showcases
- Skill tutorials

### Growth Strategies
- **Cycling Clubs**: Partner for group events
- **Zwift Community**: Target users seeking outdoor options
- **Gravel Scene**: Natural fit for exploration element
- **Local Races**: Alternative competition format
- **YouTube Influencers**: Gaming + cycling crossover

### Competitive Advantages
- **Open Source**: Community-driven development
- **Free to Play**: Lower barrier than Zwift subscription
- **Real World**: Outdoor experience vs. indoor limitations
- **Strategic Depth**: Appeals to gamers, not just fitness enthusiasts
- **Bike Variety Matters**: Gravel, road, MTB all have strategic advantages

## Positioning

### Category Creation
- Not just a "cycling app"
- Not just a "fitness game"
- **New category**: "Augmented Reality Outdoor Sport Gaming"

### Competitive Positioning Matrix
```
                    High Social/Multiplayer
                            |
                         TerraCycle
                            |
Indoor -------- Zwift --- | --- Strava -------- Outdoor
                            |
                      Traditional
                        Racing
                            |
                    Low Social/Solo
```

## Open Questions for Marketing

1. How to demonstrate gameplay before users try it?
2. How to build critical mass for multiplayer?
3. What's the hook for first-time users?
4. How to monetize while keeping free/open-source?
5. Regional vs. global launch strategy?
6. How to prevent unsafe riding behavior?
7. Balance competitive vs. casual positioning?

## Brand Personality

- **Innovative**: Pioneering new category
- **Playful**: Gaming element, not too serious
- **Inclusive**: All levels welcome
- **Strategic**: Thinking cyclists
- **Community-Driven**: Open source, collaborative
- **Adventurous**: Exploration and discovery
