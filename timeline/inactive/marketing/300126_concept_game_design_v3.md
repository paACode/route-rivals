# RouteRivals Game Design Document

**Version 3.0** | **Last Updated:** January 30, 2026
**Status:** Concept Phase | **License:** AGPLv3

---

## Executive Summary

RouteRivals transforms outdoor cycling into a real-time multiplayer sport by combining the competitive intensity of indoor cycling platforms with the adventure and authenticity of outdoor riding. Our GPS-based gaming platform turns every road into a battlefield and every ride into a strategic competition.

**The Market Gap We Fill:**
- Indoor cycling apps (Zwift, Peloton) offer real-time competition but lock you indoors
- Outdoor tracking apps (Strava) get you outside but only offer asynchronous competition
- RouteRivals delivers both: real-time outdoor competition with tactical depth

**Core Value Proposition:**
*"Real races. Real roads. Real opponents. Anytime, anywhere."*

---

## Vision & Positioning

### What We're Building

RouteRivals is the world's first real-time outdoor competitive cycling game that rewards tactical thinking, team coordination, and strategic decision-making - not just raw power and speed.

**For cyclists who:**
- Crave competition without the hassle of traditional racing
- Miss the gaming depth of Zwift but prefer outdoor riding
- Want their daily rides to feel like adventures, not chores
- Seek tactical challenges that reward cycling intelligence

**We provide:**
- On-demand competitive cycling experiences
- Real-time GPS-based gameplay with live opponents
- Multiple paths to victory beyond pure fitness
- Safe, responsible gaming that respects traffic laws

### Market Differentiation

| Platform | Real-Time | Outdoor | Tactical Depth | Team-Based |
|----------|-----------|---------|----------------|------------|
| **RouteRivals** | ✓ | ✓ | ✓ | ✓ |
| Zwift | ✓ | ✗ | Limited | ✓ |
| Strava | ✗ | ✓ | ✗ | ✗ |
| Group Rides | ✓ | ✓ | ✗ | Limited |

---

## Core Game Dynamics

### Primary Game Mode: Territory Control (2v2)

**Objective:** Two teams compete to capture and hold geographic checkpoints (flags) scattered across a real-world battle map. First team to reach victory score wins.

**What Makes This Compelling:**
- Geographic territory creates natural strategic tension
- Multiple simultaneous objectives prevent single optimal strategy
- Physical endurance meets tactical decision-making
- Works at any skill level with proper matchmaking

### The Three Pillars of Gameplay

#### 1. Territory Control - The Foundation

**How It Works:**
- 5-7 flags scattered across 5-10km battle map
- Capture flags by staying within 30-meter radius for 45 seconds
- Owned flags generate 5 points per minute automatically
- Teams must choose: defend owned flags or capture new ones?

**Strategic Depth:**
- Do you spread out to control more territory?
- Do you concentrate forces to defend key positions?
- Which flags are worth fighting for based on geography?

**Why This Works:** Mirrors real competitive cycling principles - positioning, pacing, resource management - while adding gaming structure.

#### 2. Elimination Mechanic - The Tactical Layer

**The Rule:** Overtake an opponent at speed and they're eliminated from play temporarily.

**What Counts as an Elimination:**
- You approach within 10 meters of an opponent
- You pass them with 3+ kph speed advantage
- You maintain higher speed for 5 consecutive seconds
- Clean separation achieved (15+ meters)

**Impact on Gameplay:**
- Eliminated riders must return to team base to respawn (1-3 minute penalty)
- Creates temporary 2v1 advantages for attacking team
- Eliminating player earns 25 points
- Adds high-stakes drama to every overtake

**Strategic Implications:**
- Attack opponents to create numerical advantage
- Protect teammates from elimination through positioning
- Risk vs. reward: chasing eliminations burns energy
- Defensive play: avoid being isolated and vulnerable

**Why This Works:** Transforms a simple GPS game into a tactical battle where positioning and teamwork matter as much as power output.

#### 3. Team Tactics - The Coordination Challenge

**Victory requires more than raw speed - you need strategy and teamwork.**

**Pre-Game Planning:**
Before battle begins, analyze the map with your team:
- Study terrain: main roads, single track, gravel paths
- Identify strategic flag positions
- Anticipate opponent strategies
- Assign tactical roles

**Tactical Roles in Your Team:**

**Attacker:** Hunt down opponents to create numerical advantages through eliminations

**Conqueror:** Focus on capturing and holding flags - the point generator

**Scout:** Gather intelligence on opponent positions and strategies while staying hidden

**Sprinter:** Claim sprint segments for bonus points and team buffs

**Climber:** Dominate KOM segments to earn resources for team abilities

**Bike Selection Matters:**
- Mountain bikes: Access hard-to-reach flags via single track
- Road bikes: Speed for elimination attacks and rapid flag transitions
- Gravel bikes: Versatility for mixed terrain strategies

**Why This Works:** Creates role diversity so teams need different rider types, not just four identical powerful cyclists.

---

## Secondary Objectives: Strategic Variety

Beyond core territory control, bonus objectives create multiple paths to victory.

### Green Jersey (Sprint Segments)

**What:** 2-3 designated 300-500m speed zones scattered across the map

**How to Win:**
- Fastest speed through segment earns points
- 40+ kph: 30 points
- 35-39 kph: 20 points
- 30-34 kph: 10 points

**Strategic Value:**
- Team gets checkpoint capture time buff with best overall sprint performance
- Creates "sprinter specialist" role value
- Forces decision: chase sprints or defend flags?

### King of the Mountain (Climb Segments)

**What:** 1-2 designated climbing sections (2-5 minutes of climbing)

**How to Win:**
- Timed ascent, fastest time earns points
- 1st place: 40 points
- 2nd place: 25 points
- 3rd place: 15 points

**Strategic Value:**
- Team earns resource generation buff (more sweat drops)
- Rewards climbing specialists
- Creates terrain-based tactical choices

### Exploration Waypoints

**What:** 3-5 hidden bonus locations revealed when nearby

**How to Win:**
- First player/team to reach earns 20 points
- Encourages route knowledge and exploration
- Creates "scout specialist" role value

**Strategic Value:**
- Rewards local knowledge and creative routing
- Adds discovery element to competition
- Prevents predictable gameplay patterns

### Cycling Passion (Distance & Elevation Bonus)

**What:** Biggest total distance and elevation climbed

**How to Win:**
- Team with most accumulated distance/elevation at game end: 100 bonus points

**Strategic Value:**
- Rewards constant movement and activity
- Creates late-game comeback potential
- Encourages aggressive play throughout

---

## Resource System: Sweat Drops

**Concept:** The more your team rides, the more resources you generate for tactical abilities.

**How It Works:**
- Distance traveled = sweat drops earned
- Sweat drops spent on tactical abilities
- Keep moving to unlock powerful game-changing tools

**Tactical Abilities (Using Sweat Drops):**

**Roadblock:** Force opponents to find alternate routes to checkpoints you control

**Exploration Tower:** Reveal opponent positions and movements on the map

**Temporary Revive Station:** Place strategic respawn point so eliminated teammates don't return all the way to base

**Why Resource System Works:**
- Rewards activity and movement (anti-camping mechanic)
- Creates meaningful strategic choices (which ability to use when?)
- Adds depth without breaking physical realism

---

## Game Philosophy & Balance

**Core Principle:**
*Territory control determines victory, but secondary objectives create strategic depth.*

**Balance Framework:**
- Flag control worth approximately 70% of total achievable points
- Secondary objectives worth approximately 30% of total achievable points
- You cannot ignore either completely and expect to win
- Multiple viable strategies based on team composition and terrain

**What This Means:**
- Pure flag control team can win, but secondary objectives create comeback opportunities
- Sprint/climb specialists have clear value without dominating
- Every rider type and skill level can contribute meaningfully
- Tactics and strategy can overcome pure power differences

---

## Key Features That Set Us Apart

### Real-Time Competition
- Live player tracking with GPS precision
- See opponents moving on the map in real-time
- Capture progress and dynamic scoring updates
- Immediate feedback on tactical decisions

### Strategic Gameplay
- Position yourself tactically before engagements
- Coordinate with teammates through in-game communication
- Time your attacks based on energy management
- Adapt strategy based on opponent movements

### Safety-First Design
- Traffic laws always supersede game rules
- No incentives for dangerous riding
- Mandatory safety acknowledgments before every game
- Audio/haptic feedback minimizes screen checking
- Pause button always accessible

### Accessible to All Skill Levels
- Skill-based matchmaking ensures fair competition
- Multiple roles mean different rider types can excel
- Not just about who's strongest - tactics matter
- Progressive complexity as you improve

### Community & Social Features
- Team formation and persistent rivalries
- Post-game socializing and coffee rides
- Mentorship from veteran racers
- Local leaderboards and seasonal rankings

---

## Target Audiences & Use Cases

### The Competitive Commuter (Sarah Chen)
**Pain Point:** Boring, repetitive commute routes lack motivation
**Solution:** Turn your daily commute into a competitive game with real-time opponents
**Value:** Higher intensity workouts, improved fitness, daily engagement

### The Zwift Refugee (Marcus Rodriguez)
**Pain Point:** Missing the structure and competition of Zwift racing outdoors
**Solution:** Bring gaming depth and structured competition to outdoor riding
**Value:** Real-world racing experience with Zwift-style engagement

### The Social Rider (Jennifer Thompson)
**Pain Point:** Can't find riding partners at short notice, solo rides feel lonely
**Solution:** On-demand team adventures with spontaneous matchmaking
**Value:** Social connection, route discovery, fun without intimidating competition

### The Veteran Racer (Robert Sullivan)
**Pain Point:** Wants tactical competition without race logistics and commitment
**Solution:** Accessible tactical racing that rewards experience and strategy
**Value:** Use decades of racing knowledge, mentor newer riders, stay competitive

### The Content Creator (David Kim)
**Pain Point:** Cycling content lacks drama and shareability
**Solution:** Naturally compelling moments for social media content
**Value:** Viral content opportunities, audience engagement, community growth

---

## Success Metrics & Design Goals

**Player Experience Goals:**
1. Every game feels different based on terrain and opponents
2. Wins feel earned through smart play, not just fitness
3. Losses feel like learning opportunities, not frustrations
4. Community bonds form through shared competition

**Retention Targets:**
- Day 1 return rate: 40%+
- 30-day retention: 15%+
- Average games per week: 3-5
- Net Promoter Score: 50+

**Safety Commitment:**
- Zero tolerance for unsafe gameplay incentives
- Target incident rate: <0.01% (1 per 10,000 games)
- Continuous safety monitoring and improvement
- Partnership with cycling advocacy organizations

---

## What Makes RouteRivals Special

**For Competitive Cyclists:**
Find meaningful competition without race logistics. Test your tactical skills against live opponents on real roads.

**For Zwift Refugees:**
Bring the gaming depth and structured competition outdoors. Real roads, real scenery, real cycling.

**For Social Riders:**
Spontaneous team adventures with new friends. Every ride becomes a social event with built-in structure.

**For Veteran Racers:**
Use decades of racing knowledge and tactical expertise. Mentor newer riders while scratching the competitive itch.

**For Content Creators:**
Naturally compelling moments for social media. Dramatic eliminations, close finishes, tactical masterclasses.

---

## Technical Approach

### Core Technology Stack
- **Mobile:** Flutter (cross-platform, battery-optimized)
- **Backend:** Python/FastAPI (real-time WebSocket support)
- **Database:** PostgreSQL with PostGIS (geospatial queries)
- **Caching:** Redis (real-time state management)

### Key Technical Challenges
1. **Battery Life:** Aggressive optimization to achieve 2-3 hour gameplay
2. **GPS Accuracy:** Error-tolerant mechanics with generous capture zones
3. **Real-Time Sync:** Server-authoritative gameplay with low latency
4. **Safety Features:** Comprehensive monitoring and protective systems

### Development Approach
- Open source core (AGPLv3 license)
- Community-driven development
- Iterative validation with real users
- Safety-first implementation priority

---

## Development Roadmap

**Current Phase:** Concept & Planning
**Open Source:** Yes (AGPLv3 License)
**Seeking:** Community feedback, collaborators, early testers

**MVP Focus (Months 1-18):**
- 2v2 Territory Control core gameplay
- Real-time GPS tracking and matchmaking
- Safety-first feature implementation
- Single geographic market launch (one city)

**Validation Phase (Months 6-12):**
- 50-200 beta users in launch city
- Measure retention, engagement, safety metrics
- Iterate based on user feedback
- Determine commercial viability

**Post-MVP Evolution (Year 2+):**
- Additional game modes (race, elimination, exploration)
- Advanced analytics and progression systems
- Tournament and event infrastructure
- Geographic expansion to new cities
- Monetization implementation (if validated)

---

## Business Model (Future Consideration)

**Current Status:** Open source, non-monetized during validation phase

**Potential Future Model (if commercialized):**
- **Free Tier:** 3-5 games per week, basic features
- **Premium:** $9.99/month - unlimited games, advanced stats, no ads
- **Pro:** $14.99/month - team management, custom events, coaching tools

**Key Principles:**
- No pay-to-win mechanics
- Free tier provides real value
- Premium is convenience and depth, not competitive advantage
- Community sustainability prioritized over revenue maximization

---

## Join Us

RouteRivals is an open-source project building the future of outdoor competitive cycling.

**We're Looking For:**
- Competitive cyclists to validate and test concepts
- Mobile developers (Flutter experience)
- Backend developers (Python/FastAPI)
- Game designers passionate about cycling
- Cycling safety advocates
- Early adopters willing to provide feedback

**How to Contribute:**
- Review and comment on game design concepts
- Share your cycling experience and pain points
- Test beta versions in your local area
- Contribute code or documentation
- Spread the word in cycling communities

**Get Involved:**
Visit our GitHub repository at [github.com/paACode/RouteRivals](https://github.com/paACode/RouteRivals) or reach out via issues to contribute, provide feedback, or join the development effort.

---

## Safety Commitment

**Our Promise:**
No game objective is worth compromising rider safety. Safety is not a feature - it's our foundation.

**How We Deliver:**
- Mandatory safety acknowledgments before every game
- No flags placed near dangerous intersections or high-speed roads
- Speed monitoring with automatic game pausing
- Audio/haptic feedback to minimize screen checking
- Partnership with cycling advocacy organizations
- Continuous safety monitoring and improvement
- Zero tolerance for dangerous gameplay

**Legal Framework:**
- Comprehensive terms of service and liability waivers
- Appropriate insurance coverage
- Regular legal review with cycling law specialists
- Transparency through annual safety reports

---

## Frequently Asked Questions

**Is this safe?**
Safety is our top priority. We never place objectives in dangerous locations, we enforce traffic law compliance, and we provide eyes-free gameplay through audio cues. However, you are ultimately responsible for riding safely and obeying all traffic laws.

**How is this different from Strava?**
Strava is asynchronous - you compete against past performances. RouteRivals is real-time - you compete against live opponents right now, with tactical gameplay that rewards strategy, not just speed.

**How is this different from Zwift?**
Zwift is indoors and virtual. RouteRivals brings similar gaming depth and real-time competition to outdoor riding on real roads.

**Do I need special equipment?**
Just a smartphone with GPS and data connection. Optional: heart rate monitor, power meter, smartwatch for enhanced experience.

**What if there aren't enough players near me?**
We're launching in one city initially to ensure critical mass. As we expand, we'll only enter markets where we can guarantee player density. Single-player modes against AI will also be available.

**Will this drain my battery?**
We're aggressively optimizing for battery life with a target of 2-3 hours of gameplay. External battery packs are recommended for longer sessions.

**Is this open source?**
Yes, under AGPLv3 license. This means the code is publicly available and you can contribute, but commercial derivatives must also be open source.

**When will it launch?**
We're currently in the concept phase. Realistic MVP timeline is 18-24 months with community contributions. Follow our GitHub for updates.

---

**RouteRivals - Where Cycling Meets Strategy**

*Transform outdoor cycling from a solo performance activity into a multiplayer sport*

---

## Document History

- **Version 3.0** (Jan 30, 2026): Complete rewrite with marketing positioning, clearer value propositions, improved structure
- **Version 2.0** (Jan 26, 2026): Expanded game concept with detailed mechanics and safety framework
- **Version 1.0** (Jan 24, 2026): Initial concept document
