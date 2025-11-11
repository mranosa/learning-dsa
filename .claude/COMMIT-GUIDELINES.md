# Commit Guidelines for This Project

**FOR CLAUDE:** Follow these guidelines when creating commits.

---

## Commit Message Format

### Standard Commits (Features, Fixes)

```
[Action]: Brief description

- Detailed point 1
- Detailed point 2
- Detailed point 3

[Optional context or notes]
```

**Examples:**
```
Add voice input system

- F12 hotkey with xdotool
- Voice Activity Detection with Whisper
- Auto-type into Claude Code from anywhere
```

**NO self-attribution in commits!**
- ❌ "Generated with Claude Code"
- ❌ "Co-Authored-By: Claude"
- ✅ Just the facts about what was added

---

## Session Narrative Commits (Special Format)

**When user completes a session (/next-session command):**

```
Session Complete: Day X, Session Y - [Topic]

COMPLETED:
- X/10 problems (Y marked for review)
- Problem 1: [Name] - [time]min ✅
- Problem 2: [Name] - [time]min ✅
[... all 10 listed ...]

METRICS:
- Avg time: Easy [X]min (target <15) | Medium [Y]min (target <30)
- Communication: [X]/10 | Problem Solving: [X]/10
- Code Quality: [X]/10 | Edge Cases: [X]/10
- Overall: [X.X]/10

WHAT WENT WELL:
- [Specific strength 1]
- [Specific strength 2]
- [Specific strength 3]

AREAS TO IMPROVE:
- [Specific area 1]
- [Specific area 2]
- [Specific area 3]

PATTERNS MASTERED:
✅ [Pattern] - [what learned]
⏳ [Pattern] - needs practice

VOCABULARY USED:
- Terms: [list]
- Phrases: [list]

ACTION STEPS FOR NEXT SESSION:
1. [Action 1]
2. [Action 2]
3. [Action 3]

NEXT: Day [X], Session [Y] - [Topic]

Session duration: [X]h [Y]min | Total: [total]h
Streak: Day [X] | Blind 75: [X]/75
```

**Purpose:** Learning journal in git history

---

## When to Commit

### Auto-Commits (via commands):
- `/mark-complete` → After each problem
- `/next-session` → After session with narrative
- User says "save my work" → Manual checkpoint

### Manual Commits (when building):
- After adding significant feature
- After fixing bugs
- Logical checkpoints
- Keep commits focused and atomic

---

## Commit Frequency

**During development:** Frequent small commits
**During sessions:** Auto-commits via commands
**Session ends:** One narrative commit summarizing everything

---

## Message Tone

- Clear and factual
- No unnecessary words
- No emojis in regular commits
- Use emojis only in session narratives (✅ ⏳ ⚠️)
- Professional but friendly

---

**Follow these guidelines to maintain clean, useful git history!**
