# Session 0 - System Test Checklist

Use this to verify every component of the voice interview system works.

---

## PRE-TEST: System Check

```bash
./system-check
```

**Expected:** All ✅ (xbindkeys can be ⚠️ if not started yet)

**If not all ✅:** Fix issues before continuing

---

## SETUP: Voice System Activation

```bash
./setup-voice-hotkeys && ./voice-interview
```

**Verify:**
- [ ] "Voice hotkeys activated!" message appears
- [ ] "Interactive mode active" message appears
- [ ] No errors shown

---

## TEST 1: F12 Voice Input

**From LeetCode tab (not focused on terminal):**
- [ ] Press F12
- [ ] See notification: "🎤 Listening..."
- [ ] Speak: "Test message, ok submit"
- [ ] See notification: "✅ Transcribed: Test message"
- [ ] See notification: "⚡ Auto-Submit"
- [ ] Text appears in Claude Code terminal
- [ ] Auto-submits (Enter pressed)

**If ✅:** F12 working! If ❌:** Check VOICE-SETUP.md

---

## TEST 2: TTS Voice Output

**After F12 command:**
- [ ] Hear response in Badong voice
- [ ] Audio is clear
- [ ] Response matches text shown
- [ ] No audio delays > 3 seconds

**If ✅:** TTS working! **If ❌:** Check .env for API key

---

## TEST 3: Interactive Mode Listening

**While voice-interview is running:**
- [ ] Just speak (no F12): "Testing interactive mode"
- [ ] See transcription in terminal
- [ ] Hear my voice response
- [ ] Can have conversation without F12

**If ✅:** Interactive mode working! **If ❌:** Check if ./voice-interview is running

---

## TEST 4: Start Session 0

**F12:** "Claude, start session 0 0, ok submit"

**Verify:**
- [ ] Command types into Claude
- [ ] Auto-submits
- [ ] I respond (text + voice)
- [ ] Session 0 initializes

---

## TEST 5: Problem 1 - Two Sum

### Getting Problem:
- [ ] F12: "Give me problem 1, ok submit"
- [ ] I present problem (voice + text)
- [ ] Problem details shown

### Coding in LeetCode:
- [ ] Switch to LeetCode browser tab
- [ ] Open Two Sum problem
- [ ] Code in LeetCode editor
- [ ] Think aloud: "I'm creating a hash map..."
- [ ] **I respond with voice** (Should hear me!)
- [ ] Think aloud: "The complement is..."
- [ ] **I respond** (Continuous conversation!)

### Using Vocabulary:
- [ ] Used 3+ phrases from THINKING-ALOUD-PHRASES
- [ ] Used 3+ terms from TECHNICAL-VOCABULARY
- [ ] Communication felt natural
- [ ] Had reference guides visible

### Testing:
- [ ] Click "Run" in LeetCode
- [ ] See test results
- [ ] All tests pass (or debug with F12)

### Evaluation:
- [ ] F12: "All tests pass, evaluate me, ok submit"
- [ ] Receive scores (Communication, Problem Solving, Code, Edge Cases)
- [ ] Get specific feedback
- [ ] Hear feedback via voice

---

## TEST 6: Problem 2 - Valid Palindrome

**Quick Test:**
- [ ] F12: "Next problem, ok submit"
- [ ] Solve with two pointers
- [ ] Think aloud continuously
- [ ] I respond in real-time
- [ ] Test in LeetCode
- [ ] Evaluate

---

## TEST 7: Problem 3 - Contains Duplicate

**Final Test:**
- [ ] F12: "Next problem, ok submit"
- [ ] Quick solve (hash set)
- [ ] Good communication
- [ ] Evaluate

---

## TEST 8: Session End with Narrative

**F12:** "End session, ok submit"

**Verify:**
- [ ] I provide session summary
- [ ] Git commit created
- [ ] Check commit message:
  ```bash
  git log -1 --format="%B"
  ```
- [ ] Commit has narrative format:
  - [x] COMPLETED section
  - [x] METRICS section
  - [x] WHAT WENT WELL
  - [x] AREAS TO IMPROVE
  - [x] VOCABULARY USED
  - [x] ACTION STEPS

- [ ] SESSION-HISTORY.md updated
- [ ] PROGRESS-STATE.md updated

---

## FINAL VERIFICATION

### All Components Working:
- [ ] ✅ F12 voice input (from anywhere)
- [ ] ✅ "ok submit" auto-Enter
- [ ] ✅ TTS speaks responses
- [ ] ✅ Interactive mode conversation
- [ ] ✅ LeetCode integration
- [ ] ✅ Vocabulary guides helpful
- [ ] ✅ Evaluation detailed
- [ ] ✅ Session narrative commits

### Communication Quality:
- [ ] Used thinking-aloud phrases naturally
- [ ] Used technical vocabulary correctly
- [ ] Felt comfortable explaining approach
- [ ] Responded well to probing questions

### Workflow Smooth:
- [ ] F12 worked from LeetCode
- [ ] No need to switch to terminal
- [ ] Could focus on coding
- [ ] Voice interaction felt natural

---

## Results:

**ALL CHECKED ✅:**
🎉 **System fully operational!**
📚 **Ready to start Session 1!**
🚀 **You've mastered the workflow!**

**Some issues ❌:**
⚠️ Review VOICE-SETUP.md
⚠️ Fix issues
⚠️ Re-test Session 0
⚠️ Don't start Session 1 until all ✅

---

## Next Steps

**If test passed:**
```bash
# Start the real bootcamp:
# F12: "Claude, start session 1 1, ok submit"
```

**If test had issues:**
```bash
# Check what went wrong:
cat SESSION-HISTORY.md  # Review feedback
git log -1              # Check commit narrative

# Fix and re-test
```

---

**Good luck with your test!** This is just practice - make mistakes here! 🧪
