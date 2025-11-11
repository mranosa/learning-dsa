# Voice Interview Quick Start Card

**Print this and keep at your desk!**

---

## 🖥️ Setup (Once)

```
┌─────────────────────────────────────────┐
│ Browser Tab 1: Learning Materials      │
│ (Videos, notes, docs)                  │
├─────────────────────────────────────────┤
│ Browser Tab 2: LeetCode Problem Page   │
│ (Problem + Code Editor + Test Cases)   │
├─────────────────────────────────────────┤
│ Terminal: Claude Code CLI              │
│ > ./setup-voice-hotkeys                │
│ > ./voice-interview                    │
└─────────────────────────────────────────┘
```

**One-time setup:**
```bash
cd /home/badong/Projects/learning-dsa
./setup-voice-hotkeys  # Activates F12
```

---

## 🚀 Session Flow

### 1. Start Session
**F12:** "Claude, start session 1 1, ok submit"
→ I assign video

### 2. Watch & Learn
Switch to **Browser Tab 1**, watch video (20 min)

### 3. Quiz
**F12:** "I watched the video, ok submit"
→ I quiz you (F12 to answer each question)

### 4. Get Problem
**F12:** "Give me the problem, ok submit"
→ I present problem with voice + text

### 5. Code in LeetCode
Switch to **Browser Tab 2** (LeetCode)
- Code in their editor
- **Think aloud:** "I'm creating a hash map..."
- **I respond:** "Good! What's the complexity?"
- Natural voice conversation while coding!

### 6. Test
Click **"Run"** in LeetCode → See test results

**If tests fail:**
**F12:** "Test 3 failing, ok submit"
→ I help debug

### 7. Evaluate
**F12:** "All tests pass, evaluate me, ok submit"
→ I give detailed feedback

### 8. Next
**F12:** "Next problem, ok submit"
→ Repeat steps 4-8 for all 10 problems

### 9. Complete Session
**F12:** "Next session, ok submit"
→ **Auto-commit** with full narrative!
→ Move to next session

---

## 🎤 F12 Commands

| Command | Effect |
|---------|--------|
| F12 + "Give me the problem, ok submit" | Get next problem |
| F12 + "I'm stuck, ok submit" | Get hint |
| F12 + "Evaluate me, ok submit" | Get feedback |
| F12 + "Next problem, ok submit" | Move forward |
| F12 + "My progress, ok submit" | See stats |

**Pro tip:** Add "ok submit" to auto-press Enter!

---

## 💡 Quick Tips

✅ **Think aloud** while coding (use phrases guide!)
✅ **Use technical vocabulary** (reference vocabulary guide!)
✅ **Test in LeetCode** (built-in test cases)
✅ **F12 works anywhere** (LeetCode, browser, etc.)
✅ **"ok submit" = hands-free** (auto-press Enter)

---

## 🆘 Troubleshooting

**F12 not working?**
```bash
./setup-voice-hotkeys  # Restart hotkeys
```

**Can't find Claude window?**
Make sure Claude Code CLI is running

**Voice not transcribing?**
Check microphone permissions

**See:** VOICE-SETUP.md for full troubleshooting

---

**Ready?** Run: `./setup-voice-hotkeys` then `./voice-interview`

Then: **F12** → "Claude, start session 1 1, ok submit" 🚀
