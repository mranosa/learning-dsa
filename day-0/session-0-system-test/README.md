# Session 0: System Test

**Purpose:** Verify all voice interview features before starting the real bootcamp.

**Duration:** 20-30 minutes
**Problems:** 3 easy problems
**Prerequisites:** system-check passed ✅

---

## What We're Testing

This test session verifies:
- ✅ F12 voice input (types into Claude from anywhere)
- ✅ "ok submit" auto-Enter feature
- ✅ TTS responses (I speak with Badong voice)
- ✅ Interactive mode (continuous listening while coding)
- ✅ LeetCode integration (code + test there)
- ✅ Vocabulary guides (phrases + terms)
- ✅ Evaluation system (scores + feedback)
- ✅ Session narrative commits
- ✅ Complete workflow

If everything works → Start Session 1 with confidence!

---

## Test Problems (3 Easy)

1. **Two Sum** (5-10 min)
   - Hash map pattern
   - Test F12 commands
   - Test thinking aloud

2. **Valid Palindrome** (5-10 min)
   - Two pointers pattern
   - Test interactive mode
   - Test vocabulary usage

3. **Contains Duplicate** (5 min)
   - Hash set pattern
   - Test LeetCode testing
   - Test evaluation

---

## Test Flow

### Before Starting:
```bash
./system-check  # Should show all ✅
```

### Setup:
```bash
./setup-voice-hotkeys && ./voice-interview
```

**Workspace:**
- Browser Tab 1: This README (reference)
- Browser Tab 2: LeetCode.com
- Terminal: Claude Code CLI (voice-interview running)

### Start Test:
**F12:** "Claude, start session 0 0, ok submit"

### For Each Problem:
1. **F12:** "Give me problem [1/2/3], ok submit"
2. **Open in LeetCode** (Tab 2)
3. **Code while thinking aloud** (use phrases!)
4. **Click "Run"** in LeetCode
5. **F12:** "All tests pass, evaluate me, ok submit"
6. **Review feedback**

### End Test:
**F12:** "End session, ok submit"

### Verify:
Check TEST-CHECKLIST.md - all items should be ✅

---

## Success Criteria

**All these should work smoothly:**
- [ ] F12 voice input from LeetCode
- [ ] "ok submit" auto-presses Enter
- [ ] I respond with voice
- [ ] Interactive mode listens while you code
- [ ] I respond to your thinking aloud
- [ ] LeetCode tests run successfully
- [ ] Evaluation gives scores
- [ ] Session ends with git commit

**If any fail:** See VOICE-SETUP.md for troubleshooting

**If all pass:** You're ready for Session 1! 🎉

---

## What You'll Practice

### Communication:
- Using phrases: "I think I'll use...", "The time complexity is..."
- Using terms: complement, iterate, optimal
- Thinking aloud naturally
- Responding to probing questions

### Technical:
- Hash map, two pointers, hash set patterns
- Time/space complexity analysis
- Edge case identification
- Test case verification

### Workflow:
- F12 from LeetCode
- Coding in LeetCode editor
- Testing with built-in cases
- Voice conversation with Claude

---

## After Session 0

If successful:
1. ✅ Review git commit message (should have narrative)
2. ✅ Check SESSION-HISTORY.md (narrative appended)
3. ✅ Note any improvements needed
4. ✅ **Start Session 1** for real!

If issues:
1. ⚠️ Note what didn't work
2. ⚠️ Check VOICE-SETUP.md
3. ⚠️ Fix issues
4. ⚠️ Re-test Session 0

---

**This is your dry run. Make mistakes here, learn the system, then crush Session 1!**

[See PROBLEMS.md for test problems] | [See TEST-CHECKLIST.md for verification]
