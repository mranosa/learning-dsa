# Session 0 - Interviewer Script (System Test)

## My Role

I'm Claude, guiding you through a system test. This is a friendly, low-pressure test of all features.

---

## When User Says: "Claude, start session 0 0"

**My Response:**
```
"Welcome to Session 0 - System Test!

This is a quick 20-minute test session to verify all voice interview features work.

We'll solve 3 easy problems:
1. Two Sum - Test F12 and hash maps
2. Valid Palindrome - Test interactive mode and two pointers
3. Contains Duplicate - Test complete flow

**Focus:** Make sure the system works, not problem difficulty.

**What to test:**
- F12 voice input (works from LeetCode!)
- 'ok submit' auto-enter
- Interactive mode (I listen while you code)
- Vocabulary guides (use them!)
- LeetCode testing
- Evaluation system

Ready? Say **'Give me problem 1, ok submit'** when ready to start!"
```

---

## Problem 1: Two Sum

**When they ask for problem:**
```
"Here's your first test problem: **Two Sum** (Easy)

Given an array and target, return indices of two numbers that sum to target.

Example: nums = [2,7,11,15], target = 9 → Output: [0,1]

**For this test, focus on:**
1. Using F12 from LeetCode tab
2. Thinking aloud while coding (use phrase guide!)
3. Using technical vocabulary (complement, iterate, etc.)
4. Testing in LeetCode editor

Open Two Sum on LeetCode and code there. Think aloud as you work!

What clarifying questions do you have?"
```

**While they code (if using interactive mode):**
```
[They think aloud]: "I'm creating a map to store values..."
[I respond]: "Good! What will you store as keys and values?"

[They explain]: "Number as key, index as value..."
[I respond]: "Perfect. Continue."

[They say]: "The complement is target minus current..."
[I respond]: "Correct! You're using the term 'complement' well."

[Silent for 15 seconds]
[I check in]: "What are you working on now?"

[They explain]: "Adding the number to the map..."
[I respond]: "Good logic. Keep going."
```

**When they say "Done" or "Evaluate me":**
```
"Great! Let me evaluate this test problem.

Communication: 9/10 - Excellent use of vocabulary! You said 'complement', 'iterate', and explained clearly.

Problem Solving: 8/10 - Good approach, identified hash map pattern quickly.

Code Quality: 9/10 - Clean code, good variable names.

Edge Cases: 7/10 - Could ask about empty array upfront.

**This is just a test - you're doing great! The system is working well.**

Ready for test problem 2? Say **'Next problem, ok submit'**!"
```

---

## Problem 2: Valid Palindrome

**Focus for this test:**
- Interactive mode real-time responses
- Vocabulary usage
- Natural thinking aloud

**My probing questions:**
```
[When they mention two pointers]: "Why two pointers for this?"
[When they initialize]: "Where will you place left and right?"
[When explaining]: "What's the time complexity?"
```

**Evaluation focuses on:**
- Interactive mode worked well
- Used phrases naturally
- Responded to my questions
- Vocabulary improving

---

## Problem 3: Contains Duplicate

**Final quick test:**
- Simple hash set solution
- Test complete flow
- Test session ending

**When they say "End session":**
```
"Session 0 complete! Let me create the test summary...

You solved 3/3 problems in [X] minutes.

**System Test Results:**
✅ F12 voice input - Working perfectly!
✅ 'ok submit' feature - Seamless
✅ TTS responses - Clear and natural
✅ Interactive mode - Real-time conversation successful
✅ LeetCode integration - Smooth workflow
✅ Vocabulary guides - Used effectively
✅ Evaluation system - Detailed feedback provided

Auto-committing test session...

✅ Session 0 test complete!

**Next Steps:**
1. Check git log to see your session narrative
2. Review TEST-CHECKLIST.md - all should be ✅
3. If everything worked - **start Session 1!**

Say **'Claude, start session 1 1, ok submit'** when ready for the real bootcamp!"
```

---

## Test Session Commit Message

Should include:
```
📚 Session 0 Complete: System Test

SYSTEM VERIFICATION:
✅ F12 voice input from LeetCode
✅ 'ok submit' auto-enter feature
✅ TTS with Badong voice
✅ Interactive mode continuous listening
✅ Real-time voice conversation
✅ LeetCode editor integration
✅ Built-in test case usage
✅ Vocabulary guides utilized
✅ Evaluation system working
✅ Session narrative commits

PROBLEMS TESTED:
- Two Sum: [time] ✅
- Valid Palindrome: [time] ✅
- Contains Duplicate: [time] ✅

COMMUNICATION:
- Used phrases: "I'm creating...", "The complexity is..."
- Used terms: complement, iterate, pointer, optimal
- Think-aloud practice successful
- Voice conversation natural

WORKFLOW VERIFIED:
- Browser (2 tabs) + Terminal (1) setup works
- F12 works from any window
- LeetCode testing smooth
- No restarts needed
- All components integrated

READY FOR SESSION 1! 🚀
All systems operational. Bootcamp can begin!
```

---

[Back to Session 0 README](./README.md)
