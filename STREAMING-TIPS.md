# Streaming Tips & Setup Guide

How to stream your DSA learning effectively with Claude as your interviewer.

---

## Setup

### Required
- **TTS (Text-to-Speech)** enabled in Claude settings
- **Screen layout:** VSCode (left) + Browser/LeetCode (right)
- **Timer visible** on screen
- **Webcam** (optional but recommended)
- **Good microphone**

### Recommended
- **OBS Studio** or streaming software
- **Two monitors** (one for you, one for stream output)
- **Cheatsheet printed** and visible
- **Water** nearby!

---

## Screen Layout

### Option 1: Split Screen
```
┌─────────────────────────────────┐
│                                 │
│         VSCODE (Code)           │
│                                 │
├─────────────────────────────────┤
│                                 │
│    Browser (Problem + Chat)     │
│                                 │
└─────────────────────────────────┘
```

### Option 2: Side by Side
```
┌──────────────────┬──────────────────┐
│                  │                  │
│      VSCODE      │     Browser      │
│      (Code)      │   (Problem +     │
│                  │      Chat)       │
│                  │                  │
└──────────────────┴──────────────────┘
```

### What to Show
- ✅ Code editor (large font!)
- ✅ Problem statement
- ✅ Timer countdown
- ✅ Current problem (e.g., "Problem 3/10")
- ⚠️ Hide: Personal info, API keys, passwords

---

## Before Stream

### Warm-up Routine (10 min)
1. Review previous day's feedback
2. Review today's session topic
3. Practice thinking aloud with one problem
4. Test TTS with Claude
5. Check audio levels

### Stream Title Ideas
- "Day 1: Learning Big O & Arrays - Interactive Interview Practice"
- "Blind 75 Grind - Session 3: Sliding Window Patterns"
- "Live DSA Interview Prep with AI Interviewer"
- "1-Week Coding Bootcamp - Day 2/7"

---

## During Stream

### Starting the Stream
```
1. Greet viewers
2. Explain today's topic
3. Show session goals (X problems)
4. Say: "Claude, start session [day] [session]"
5. Watch assigned video (on or off stream)
6. Say: "Claude, I watched the video"
```

### Think Aloud Technique

**Good Example:**
```
"I'm reading the problem... okay, it wants me to find two numbers
that sum to target. Let me think about the constraints... the array
is unsorted, so I can't use two pointers directly. I need O(1)
lookup... that means hash map. Let me ask some clarifying questions..."
```

**Bad Example (Silent Coding):**
```
*types code silently for 5 minutes*
*no explanation*
*viewers have no idea what you're thinking*
```

### Engaging with Chat

**Do:**
- Pause between problems to answer questions
- Use "Claude, pause" when reading chat
- Acknowledge good questions
- Explain your reasoning to viewers

**Don't:**
- Get distracted mid-problem
- Argue with chat
- Let chat give away solutions
- Break focus during coding

### Using Voice Commands

Make it natural:
```
"Alright, I'm stuck here. Claude, give me a hint."
[Wait for Claude's response]
"Ah, that's a good nudge. Let me think about hash maps..."

"I think I'm done. Claude, I'm done coding."
[Claude asks you to walk through solution]
"Sure, let me trace through the example..."
```

---

## Interview Simulation Mode

### Treat Each Problem as Real Interview

**Before coding:**
```
You: "Let me make sure I understand the problem..."
[Restate problem]
You: "Can I ask a few clarifying questions?"
[Ask about edge cases, constraints]
You: "I'm thinking this is a hash map problem because..."
[Explain pattern recognition]
You: "Let me outline my approach before coding..."
[Discuss brute force, then optimal]
You: "Does this approach make sense? Should I proceed?"
[Get Claude's approval]
```

**During coding:**
```
"I'm creating a hash map to store values I've seen..."
"Now I'll loop through the array once..."
"For each number, I'll calculate the complement..."
"If complement exists in my map, I found the pair..."
```

**After coding:**
```
You: "Claude, I'm done coding."
Claude: "Walk me through your solution with an example."
You: [Trace through code step by step]
You: "Claude, evaluate me."
Claude: [Gives structured feedback]
```

### Handling Pressure

**When stuck:**
```
✅ "I'm stuck. Let me take a moment to think..."
✅ "Claude, I'm stuck. Can you ask me some probing questions?"
✅ "Let me step back and reconsider the pattern..."

❌ Don't: Get flustered, apologize excessively, give up
```

**When timer running low:**
```
✅ "I have 5 minutes left. Let me prioritize getting a working solution..."
✅ "Running low on time. I'll explain what I'd do next..."

❌ Don't: Panic, rush without thinking, code sloppily
```

---

## Streaming-Specific Commands

### For Viewers
- **"Claude, explain for viewers"** - I explain concept to audience
- **"Claude, summarize so far"** - Recap for new viewers
- **"Claude, what should I ask"** - I suggest good clarifying questions

### Managing Flow
- **"Claude, pause"** - Save state, take break, read chat
- **"Claude, time check"** - Show remaining time
- **"Claude, where are we"** - Recap current status

---

## Scene Setup (OBS)

### Scene 1: Intro
- Webcam (large)
- Today's topic overlay
- Session number
- Goals for today

### Scene 2: Problem Solving (Main)
- Code editor (60% of screen)
- Browser/Problem (30% of screen)
- Webcam (small corner, 10%)
- Timer overlay
- Current problem counter

### Scene 3: Feedback
- Webcam (larger)
- Evaluation rubric overlay
- Score display
- Action items text

### Scene 4: Break
- "Be Right Back" screen
- Countdown timer
- Music (optional)

---

## Overlay Elements

### Must Have
- **Timer** - countdown for current problem
- **Problem Counter** - "Problem 3/10"
- **Session Info** - "Day 1, Session 2: Hash Maps"
- **Progress** - "15/120 problems completed"

### Nice to Have
- **UMPIRE Checklist** - check off steps as you go
- **Current Pattern** - "Two Pointers"
- **Score** - overall average score
- **Streak** - "Day 3 streak"

---

## Interaction Tips

### Starting a Problem
```
"Alright chat, here comes problem 5. This is a medium difficulty
problem about... let me read it first before Claude presents it.

Claude, give me the problem."
[Claude reads problem]

"Okay, so we need to find... let me ask clarifying questions first."
```

### Explaining to Chat
```
"For those just joining, we're using a technique called sliding window.
The idea is we maintain a window of elements and slide it across the
array. It's useful when we need to find subarrays or substrings.

The key insight is... [explain]

Claude, can you explain for viewers?"
[Claude gives beginner-friendly explanation]
```

### Handling Wrong Answer
```
✅ "Hmm, that didn't work. Let me debug this..."
✅ "I missed something. Let me trace through again..."
✅ "Claude, what did I miss?"

❌ "Ugh, I'm so bad at this..."
❌ "This problem is stupid..."
❌ *Rage quit*
```

---

## Post-Problem Routine

### After Each Problem
1. **"Claude, evaluate me"** - Get feedback
2. Read feedback on stream
3. Discuss with chat what you learned
4. Note action items for next problem
5. **"Claude, mark complete"** - Auto-commit
6. Take 2-min break (stretch, water)
7. **"Claude, next problem"** or **"Claude, next session"**

### After Each Session
1. **"Claude, my progress"** - Show stats
2. Discuss with chat:
   - What patterns you learned
   - What was hardest
   - What improved
3. Preview next session
4. Thank viewers
5. Save VOD for review

---

## Common Streaming Mistakes

### ❌ Don't Do This
- Silent coding for long periods
- Ignoring chat completely
- Getting tilted by mistakes
- Skipping problems without trying
- Not explaining your thought process
- Bad audio quality
- Screen text too small to read
- Forgetting to start timer

### ✅ Do This Instead
- Think aloud constantly
- Engage with chat between problems
- Treat mistakes as learning opportunities
- Attempt every problem (hints are okay!)
- Explain every decision
- Test audio before stream
- Font size 16-20pt minimum
- Use visible timer overlay

---

## Viewer Engagement

### Encourage Participation
- "Chat, what pattern do you think this is?"
- "Anyone else get stuck on this problem?"
- "What approach would you use?"
- Poll: "Should I use approach A or B?"

### Respond to Questions
- Pause between problems to answer
- Use "Claude, pause" to maintain state
- Acknowledge insightful comments
- Don't let chat give away full solutions

### Build Community
- Regular streaming schedule
- Discord for off-stream discussion
- Celebrate milestones together
- Share resources
- Review each other's solutions

---

## Technical Issues

### If TTS Stops Working
1. Refresh Claude
2. Check TTS settings
3. Fallback: Read Claude's responses aloud
4. Continue session (state is saved!)

### If Stream Drops
1. Don't panic
2. Use **"Claude, save my work"**
3. Reconnect stream
4. Use **"Claude, resume"** to continue
5. Explain to viewers what happened

### If You Need a Break
```
"I need a quick break. Claude, pause timer."
[Take 5-10 min break]
"Back! Claude, resume."
```

---

## Authenticity Tips

### Be Yourself
- Show your struggle - it's relatable!
- Celebrate small wins
- Admit when you don't know something
- Ask Claude for explanations
- Learn in public

### Good Phrases
- "I'm not sure about this, let me think..."
- "That's a good question from chat, Claude can you explain?"
- "I learned something new today!"
- "This is harder than I thought, but that's okay"

### Avoid
- Pretending to know everything
- Getting defensive about mistakes
- Comparing yourself to others
- Faking understanding

---

## Sample Stream Schedule

### 3-Hour Stream
```
00:00 - 00:10: Intro, greet viewers, review yesterday
00:10 - 00:30: Watch video, concept check
00:30 - 01:00: Problems 1-2 (Easy)
01:00 - 01:50: Problems 3-5 (Medium)
01:50 - 02:00: Break
02:00 - 02:50: Problems 6-8
02:50 - 03:00: Review progress, Q&A, outro
```

---

## Motivation

### Why Stream Your Learning?

**Benefits:**
- **Accountability** - harder to skip practice
- **Community** - learn with others
- **Portfolio** - VODs show your progress
- **Communication** - practice explaining
- **Feedback** - viewers catch your mistakes
- **Motivation** - viewers cheer you on

**Remember:**
- Everyone starts somewhere
- Struggling is part of learning
- Your journey helps others
- Progress > perfection

---

## Quick Checklist

**Before Stream:**
- [ ] TTS enabled
- [ ] Screen layout ready
- [ ] Timer visible
- [ ] Cheatsheet printed
- [ ] Audio tested
- [ ] Warm-up problem done
- [ ] Water ready

**During Stream:**
- [ ] Think aloud constantly
- [ ] Engage with chat
- [ ] Use UMPIRE method
- [ ] Get feedback after each problem
- [ ] Take breaks
- [ ] Stay positive

**After Stream:**
- [ ] Save VOD
- [ ] Note improvements for next time
- [ ] Thank viewers
- [ ] Commit progress
- [ ] Rest!

---

**Now go stream and learn!** 🎥🚀

[Back to README](./README.md)
