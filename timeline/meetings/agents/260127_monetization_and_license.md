# Founder Meeting: Hobby vs. Monetization

**Date:** 2026-01-27
**Attendees:** Founder, Senior Software Architect (AI), Marketing Specialist (AI), Game Design Expert (AI)
**Topic:** Should Route Rivals be a fun project or a monetized product?

---

## Meeting Context

The founder called a strategic meeting with three expert advisors to discuss the fundamental direction of Route Rivals: build it as a hobby/fun project, or pursue serious monetization.

---

## Expert Perspectives

### Senior Software Architect

**Current State Assessment:**
- Project is in conception phase (no code written yet)
- Comprehensive planning documentation exists (market research, personas, use cases, technical architecture)
- Proposed tech stack: Flutter (mobile) + Python/FastAPI (backend) + PostgreSQL/PostGIS + Redis

**Cost Comparison:**

| Path | Cost | Timeline |
|------|------|----------|
| Hobby Project | $50-100 | 6-8 weeks |
| Commercial Product | $90-150K | 10-12 weeks + polish |

**Key Insight:** The project sits in a "dangerous middle ground" - too technically complex for a true hobby (real-time multiplayer, geospatial queries, WebSockets), but too risky for $100K+ investment without validation.

**Recommendation:** Hybrid validation approach - spend $10-15K on validation first (6-8 weeks), then decide.

---

### Marketing Specialist

**Market Opportunity:**
- Real gap exists between Zwift (indoor) and Strava (async)
- Target users already spend $140-340/year on cycling apps
- Potential: $5-50M ARR with strong execution

**Proposed Pricing Model:**
- FREE: 3-5 games/week (growth engine)
- PREMIUM: $9.99/month (core revenue)
- PRO: $14.99/month (power users)

**Recommendation:** Build with commercial intent, but don't charge for first 6-12 months while validating.

---

### Game Design Expert

**Core Loop Assessment:** 7.5/10 - commercially viable with execution risk

**Critical Concerns:**
1. Cold start problem (need player density per geographic area)
2. Safety design (existential risk if not addressed)
3. Battery optimization (poor battery = killed reviews)

**Recommendation:** Start as "serious hobby with commercial option value" - launch in ONE city with 50-200 users, validate, then decide.

---

## Initial Consensus

All three experts converged on a **Validated Hybrid Approach**:

1. Don't commit to full commercial yet
2. Don't treat it as pure hobby either
3. Build seriously, validate with real users
4. Make commercial decision based on data

**Proposed Validation Metrics:**
- 40%+ 30-day retention
- 3+ games per user per week
- NPS 40+
- Zero safety incidents

---

## Critical Constraint Revealed

**Founder's available time: ~2 hours per week**

This fundamentally changed the discussion.

### The Math Problem

- Current vision (real-time multiplayer GPS cycling game) = 500-800 hours minimum
- At 2h/week = **5-8 years to MVP**

---

## Open Source Discussion

### Should Route Rivals be open source?

**Decision: YES**

**Rationale:**
- At 2h/week, need help more than secrecy
- Attracts collaborators (best path forward)
- Validates interest before investing years
- Creates portfolio value even if incomplete
- Community can improve the work

### License Choice: AGPLv3

| License | Verdict | Rationale |
|---------|---------|-----------|
| **AGPLv3** | Recommended | Prevents cloning backend as service without contributing back |
| GPL v3 | Alternative | Same protection, but doesn't cover network services |
| MIT/Apache | Avoid | Too vulnerable at 2h/week - someone could clone and out-execute |

---

## Co-Founder Update

**New Development:** Founder will have a co-founder who is a software developer

**Co-founder Details:**
- Availability: 2-4 hours/week
- Background: Software engineering graduate
- Alignment on monetization: Not yet discussed

**Combined Capacity:** ~4-6 hours/week

---

## Updated Recommendations

### Revised Timeline
- Realistic MVP: 18-24 months at 4-6h/week combined

### Tech Stack (Confirmed)
- Mobile: Flutter
- Backend: Python/FastAPI
- Database: PostgreSQL/PostGIS
- Caching: Redis

### Suggested Division of Work

| Founder | Co-founder |
|---------|------------|
| Product vision & game design | Mobile app (Flutter) |
| Market research & user feedback | Backend basics (Python/FastAPI) |
| Community & outreach | Infrastructure & deployment |
| Documentation & planning | Code implementation |

### Scope Recommendation
- Start with async challenges (no real-time)
- Add multiplayer later if traction achieved

---

## Critical Next Steps

### Immediate (Before Any Code)

1. **Co-founder alignment conversation:**
   - Hobby or business?
   - Equity split (get in writing)
   - Decision-making process
   - Exit scenarios

2. **Project setup:**
   - Add AGPLv3 LICENSE file
   - Update README with "hobby project - collaborators wanted" disclaimer
   - Create COLLABORATORS_WANTED.md
   - Push to GitHub public
   - Share in cycling + dev communities

---

## Action Items

| Action | Owner | Priority |
|--------|-------|----------|
| Have alignment conversation with co-founder | Founder | Critical |
| Agree on equity/decision-making structure | Both | Critical |
| Set up GitHub repo with AGPLv3 license | Co-founder | High |
| Create COLLABORATORS_WANTED.md | Founder | Medium |
| Post to cycling/dev communities | Founder | Medium |

---

## Key Decisions Made

1. **Open Source:** Yes, with AGPLv3 license
2. **Monetization:** Defer decision until validation complete
3. **Scope:** Start simple (async), add complexity later
4. **Timeline:** 18-24 months to MVP (realistic)

---

## Next Meeting

Agenda for next session:
- Review co-founder alignment discussion outcomes
- Finalize equity/governance structure
- Set up project infrastructure (GitHub, CI/CD, etc.)
- Define MVP scope in detail
