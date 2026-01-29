# CLA vs No CLA Analysis

**Date:** 2026-01-29
**Context:** Researching whether Route Rivals needs a Contributor License Agreement

---

## Case Study: Habitica

Habitica is an open-source gamified habit tracker that monetizes successfully **without a CLA**.

### Habitica's Licensing
- **Code:** GPL v3
- **Assets:** CC-BY-NC-SA 3.0
- **CLA:** None

### Habitica's Revenue Model
- Gems (in-app currency)
- Subscriptions
- Premium features

---

## Why Habitica Doesn't Need a CLA

| Revenue Source | Requires CLA? | Why? |
|----------------|---------------|------|
| Gems/Subscriptions | No | They sell in-app currency, not the code |
| Hosting the service | No | GPL lets anyone run the code, but users pay Habitica for convenience |
| Premium features | No | Features run on their servers |

**Key insight:** They don't sell the software - they sell access to their hosted service and virtual goods. The code being GPL doesn't prevent this.

---

## Route Rivals: CLA vs No CLA

### With CLA (Current Choice)

**Pros:**
- Can dual-license later (offer commercial license to enterprises)
- Can switch to different license if needed
- Maximum future flexibility

**Cons:**
- Some open-source contributors dislike CLAs
- May reduce contributions slightly
- Extra complexity

### Without CLA (Habitica Model)

**Pros:**
- Simpler for contributors
- More "pure" open-source approach
- Works fine for service-based monetization

**Cons:**
- Cannot easily relicense
- Cannot offer proprietary version to enterprises
- Limited flexibility if business model changes

---

## How Route Rivals Could Monetize (No CLA Required)

1. **Freemium model** - Free tier vs. paid tiers
2. **In-app purchases** - Cosmetics, team slots, etc.
3. **Server-side features** - Premium matchmaking, analytics, leagues
4. **Subscriptions** - Monthly/yearly premium access

The code is open, but **your servers, your users, your brand** are not.

---

## When Would You Need a CLA?

Only if you want to:
- Sell the software itself (license to enterprises)
- Switch to a different license entirely
- Offer a proprietary version to companies who can't use AGPL

For a gaming service like Route Rivals, these scenarios are unlikely.

---

## Decision

**Keep CLA for now.**

Rationale:
- Doesn't hurt to have it
- Provides flexibility if business model changes
- Can remove later if contributors push back
- Early stage = few contributors = low friction

---

## Current Route Rivals Licensing Setup

| Component | License |
|-----------|---------|
| Code | AGPLv3 |
| Assets | CC-BY-NC-SA 4.0 |
| Contributions | CLA (allows relicensing) |

Files:
- `LICENSE` - Main license file with all terms
- `CONTRIBUTING.md` - Detailed CLA terms for contributors
