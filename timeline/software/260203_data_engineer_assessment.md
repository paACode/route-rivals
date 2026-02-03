# Data Engineer Assessment: Expert Consensus

**Date:** 2026-02-03
**Reviewers:** Senior Software Architect & Game Design Expert
**Question:** Does Route Rivals need a Data Engineer?

---

## Verdict: Not Now, But Eventually Yes

| Phase | Users | Data Engineer Needed? |
|-------|-------|----------------------|
| MVP/Prototype | 0-100 | **No** |
| Beta | 100-2,000 | **Part-time analyst** |
| Launch | 5,000+ | **Yes (full-time)** |
| Scale | 10,000+ | **Data team (2-3)** |

---

## Senior Software Architect's View

### Why Not Now

- Your workload is I/O bound, not data-pipeline heavy
- PostGIS queries and Redis caching are standard backend skills
- FastAPI handles your scale easily (<10% capacity at 5K users)
- Firebase Analytics provides out-of-the-box insights
- A backend developer with SQL skills can handle current needs

### When to Hire

- Beyond 50K concurrent users (database sharding needed)
- Advanced analytics (churn prediction, route recommendations)
- Real-time processing at scale (thousands of simultaneous GPS traces)
- ML features (ghost racing AI, player behavior models)

---

## Game Design Expert's View

### Why Not Now

- Manual playtests reveal more than unexamined logs at prototype stage
- Basic balance metrics (capture rates, win distribution) are simple SQL queries
- Focus should be on product validation, not data sophistication

### Why Eventually Essential

1. **Game Balance** - Tuning 45-second capture times, point values, skill costs requires statistically significant data

2. **Safety Analytics (Critical)** - You MUST prove the game doesn't encourage dangerous behavior. Legal defense requires data infrastructure showing you monitored and mitigated risks

3. **Data-Driven Features:**
   - Ghost racing (route matching algorithms, compression)
   - AI opponents (ML models trained on player movement)
   - Anti-cheat (outlier detection on leaderboards)
   - Community events (predictive attendance analytics)

---

## Future Data Engineer Role

### Responsibilities

- Build ETL pipelines (PostgreSQL → Data Warehouse)
- Implement geospatial analytics (player density clustering, heatmaps)
- Safety anomaly detection (dangerous speed patterns, high-risk flag locations)
- ML-powered features (ghost racing, AI opponents, matchmaking optimization)
- A/B testing infrastructure for game balance
- Real-time leaderboard computation and anti-cheat

### Required Skills

- PostGIS/GIS expertise
- Python data stack (pandas, scikit-learn)
- Time-series databases (TimescaleDB)
- Basic ML (clustering, anomaly detection)
- Stream processing (Kafka, Redis Streams)

### Salary Range

$80,000-120,000/year (varies by location)

---

## Immediate Action (No Hire Required)

Both experts strongly recommend **instrumenting everything now**:

```python
# Log every game event from day 1
{
    'timestamp': '2026-02-03T14:32:10Z',
    'event_type': 'flag_captured',
    'game_id': 'uuid',
    'player_id': 'uuid',
    'metadata': {
        'capture_duration': 47.3,
        'location': {'lat': 47.1234, 'lng': 8.5678}
    }
}
```

**Why:** The cost of not having data when you need it is redesigning blind. Log now, analyze later.

---

## Phased Data Strategy

### Phase 1: Prototype (Now)

- **Data Role:** None dedicated
- **Who Does It:** Senior architect (basic logging, ad-hoc queries)
- **Investment:** 5-10 hours/week
- **Tools:** PostgreSQL, Python pandas, Jupyter

### Phase 2: Beta (50-500 users)

- **Data Role:** Part-time Data Analyst
- **Who:** Contractor, 20 hrs/week
- **Investment:** $3,000-6,000/month
- **Tools:** + Grafana, Metabase, basic Python scripts

### Phase 3: Growth (1,000-10,000 users)

- **Data Role:** Full-time Data Engineer
- **Who:** Hire #5 or #6 (after first mobile developer)
- **Investment:** $80,000-120,000/year
- **Tools:** + TimescaleDB, Apache Superset, ML pipelines

### Phase 4: Scale (10,000+ users)

- **Data Role:** Data Engineering Team (2-3 people)
- **Who:** Lead Data Engineer + ML Engineer + Analytics Engineer
- **Investment:** $200,000-300,000/year
- **Tools:** Full data warehouse, real-time processing, advanced ML

---

## Key Metrics to Track from Day 1

### Game Balance

- Flag capture success rate (target: 60-80%)
- Average game duration (target: 60-90 minutes)
- Win condition distribution (territory vs bonuses)
- Skill usage frequency

### Player Engagement

- Session length
- Return rate (7-day, 30-day)
- Games per user per week
- Social connections (friends added)

### Safety (Critical)

- Max speed per session
- Speed violations (>40 km/h in restricted zones)
- Incident reports
- GPS accuracy (standard deviation from road)

### Technical Performance

- Battery drain per hour
- GPS update frequency
- WebSocket connection stability
- API response times

---

## Bottom Line

Your current team (Senior Architect + backend developers) can handle data needs through beta. Hire a **part-time Data Analyst** at ~500 users, and a **full-time Data Engineer** when you hit 5,000+ users and need ML features or safety analytics at scale.

The real risk isn't hiring too late - it's failing to log the right data early. Start logging now, hire analytical talent when the volume demands it.
