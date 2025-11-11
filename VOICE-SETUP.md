# Voice Interaction Setup & Usage Guide

Complete guide to using the interactive voice interview system.

---

## 🎯 What You Have

### Voice OUTPUT (TTS) ✅
- **I speak ALL my responses** using your Badong voice
- **Automatic** - happens on every message
- **ElevenLabs Turbo v2.5** - fast, high-quality
- **Smart text cleaning** - says "code on screen" instead of reading code blocks

### Voice INPUT (STT) ✅
- **Continuous listening** during problem-solving
- **Whisper-based transcription** - highly accurate
- **Voice Activity Detection** - auto-starts/stops recording
- **Hands-free** - just speak naturally

### Interactive Mode ✅
- **Real-time conversation** while coding
- **I respond to your questions** immediately
- **Probing questions** like real interviewer
- **Silence check-ins** if you're quiet too long

---

## 🚀 Quick Start

### Method 1: Interactive Coding Mode (Recommended)

**1. Start a session:**
```bash
# Regular way (typing)
/start-session 1 1
```

**2. After getting the problem, activate voice mode:**
```bash
./.claude/hooks/interactive_mode.py start
```

**3. Start thinking aloud while coding:**
- "I'm going to use a hash map for this..."
- "Let me loop through the array..."
- "What if the array is empty?" *(I'll respond!)*
- "I think the time complexity is O of n..."

**4. I respond in real-time:**
- "Good choice! What's the complexity?"
- "How will you handle that edge case?"
- "Keep going."

**5. When done:**
- Say: "I'm done coding"
- I'll guide you through testing

### Method 2: Manual Voice Input

**Use voice detector directly:**
```bash
# Speak into mic, get transcription
./. claude/hooks/utils/voice_detector.py
```

Then copy/paste the transcription into Claude Code.

---

## 🎤 How Voice Commands Work

### Automatic Recognition

When you speak any of these, they're automatically converted to commands:

| What You Say | Command Triggered | What Happens |
|--------------|-------------------|--------------|
| "Claude, start session 1 1" | `/start-session 1 1` | Starts session |
| "Give me the problem" | `/problem` | I present problem |
| "I'm stuck" | `/hint` | Level 1 hint |
| "Give me a hint" | `/hint` | Level 1 hint |
| "Evaluate me" | `/evaluate` | Full feedback |
| "Next problem" | Next problem | Moves forward |
| "My progress" | `/my-stats` | Shows dashboard |

**Shortcuts:**
- "Go" → Give me the problem
- "Hint" → Give me a hint
- "Done" → I'm done coding
- "Next" → Next problem
- "Stats" → My progress

---

## 🗣️ During Interactive Coding

### What to Say (Think Aloud):

```
"I'm creating a hash map to store values I've seen..."
→ I respond: "Good. What's the complexity?"

"O of n for time, O of n for space"
→ I respond: "Correct! Keep going."

"Let me loop through the array with index i..."
→ I respond: "Mm-hmm."

"I'm checking if complement exists in the map..."
→ I respond: "What happens if it doesn't exist?"

"Then I add the current number to the map..."
→ I respond: "Good logic."
```

### Questions I Might Ask:

- "What's the time complexity of that approach?"
- "How are you handling edge cases?"
- "What if the input is empty?"
- "Can you explain that logic?"
- "What happens at this line?"

### If You're Silent > 30 Seconds:

Me: "You've been quiet. Can you talk me through what you're thinking?"

**This simulates a real interview!** Interviewers want continuous communication.

---

## ⚙️ Configuration

### Adjust Voice Detection Settings

Edit `.claude/hooks/utils/voice_config.json`:

```json
{
  "whisper_model": "base",           // tiny, base, small, medium
  "language": "en",                  // en, auto, etc.
  "silence_threshold": 0.01,         // Lower = more sensitive
  "silence_duration": 1.5,           // Seconds of silence to stop
  "min_recording_duration": 0.5,    // Minimum valid recording
  "max_recording_duration": 30       // Maximum per recording
}
```

**Tuning Tips:**
- **Too sensitive** (picks up background noise): Increase `silence_threshold` to 0.02-0.03
- **Not sensitive enough** (misses quiet speech): Decrease to 0.005-0.008
- **Cuts off too early**: Increase `silence_duration` to 2.0-2.5
- **Waits too long**: Decrease to 1.0

### Adjust TTS Settings

Edit `.claude/tts-config.json`:

```json
{
  "enabled": true,
  "voiceName": "Badong",
  "modelId": "eleven_turbo_v2_5",
  "stability": 0.5,                 // 0-1 (higher = more stable)
  "similarityBoost": 0.8,           // 0-1 (higher = more like sample)
  "speakAssistantMessages": true,
  "speakNotifications": true,
  "speakCompletions": true
}
```

---

## 🛠️ Commands Reference

### Start Interactive Mode
```bash
./.claude/hooks/interactive_mode.py start
```

### Stop Interactive Mode
```bash
# Say this: "Claude, pause"
# Or manually: ./.claude/hooks/interactive_mode.py stop
```

### Check Status
```bash
./.claude/hooks/interactive_mode.py status
```

### Test Voice Detection Only
```bash
./. claude/hooks/utils/voice_detector.py
# Speak into mic, see transcription
```

### Test Command Parser
```bash
./. claude/hooks/utils/command_parser.py test
# See all command patterns
```

---

## 📺 Streaming Setup

### Recommended OBS Setup

**Audio Sources:**
1. **Microphone** - Your voice input
2. **Desktop Audio** - My voice output (ElevenLabs TTS)

**Scenes:**
1. **Problem Solving** (Main):
   - VSCode (60% screen)
   - Browser/LeetCode (30%)
   - Webcam (10%, corner)
   - Timer overlay
   - Transcription overlay (optional)

**Overlays:**
- Real-time transcription (what you just said)
- Current problem counter
- Timer
- Session info

---

## 🎬 Typical Voice Interview Session

```
You: "Claude, start session 1 1"
Me: "Starting Day 1, Session 1: Big O & Arrays. Watch this 20-min video..."

[You watch video]

You: "I watched the video"
Me: "Great! Let's do a quiz. Question 1: Explain Big O notation..."

You: "Big O describes how runtime scales with input size..."
Me: "Excellent! Question 2: What's the time complexity of..."

[After quiz]

Me: "Ready for problems? Say 'give me the problem' or 'go'."

You: "Give me the problem"
Me: "Here's your problem: Two Sum. Given an array of integers..."

You: "Can the array be empty?"
Me: "Great question! Array has at least 2 elements."

You: "Is it sorted?"
Me: "No, the array is not sorted."

You: "Okay, I think I'll use a hash map for O of 1 lookups"
Me: "Good approach! What's the overall complexity?"

You: "O of n time because I loop once, O of n space for the map"
Me: "Correct! Proceed with your implementation."

[You activate interactive mode]

You (typing): ./.claude/hooks/interactive_mode.py start

[Now just speak while coding]

You: "I'm creating a map to store values I've seen..."
Me: "Mm-hmm."

You: "Looping through the array with index i..."
Me: "How many iterations?"

You: "N iterations, once through the array"
Me: "Good."

You: "Calculating complement as target minus current number..."
Me: "What happens if complement exists in your map?"

You: "Then I found the pair, return both indices..."
Me: "Excellent logic. What if it doesn't exist?"

You: "I add the current number to the map with its index..."
Me: "Perfect. Keep implementing."

[Continue natural conversation]

You: "I'm done coding"
Me: "Great! Walk me through your solution with the example..."

[You trace through code verbally]

You: "Evaluate me"
Me: "Let me evaluate your performance. Communication: 9 out of 10..."

[I give detailed feedback]

You: "Next problem"
Me: "Moving to problem 2: Best Time to Buy and Sell Stock..."
```

---

## 🐛 Troubleshooting

### TTS Not Working

**Check:**
1. `ELEVENLABS_API_KEY` in `.env` file
2. Test directly: `./.claude/hooks/elevenlabs_tts.py "test"`
3. Check API quota at elevenlabs.io
4. Verify audio output device

**Fix:**
```bash
# Check .env
grep ELEVENLABS_API_KEY .env

# Test TTS
./.claude/hooks/elevenlabs_tts.py "Testing voice"

# Check audio devices
pactl list sinks short  # Linux
```

### Voice Detection Not Working

**Check:**
1. Microphone permissions
2. `sounddevice` can access mic
3. Audio input device

**Fix:**
```bash
# Test microphone
whisper-env/bin/python3 -c "import sounddevice as sd; print(sd.query_devices())"

# Test recording
whisper-env/bin/python3 -c "
import sounddevice as sd
import numpy as np
rec = sd.rec(int(2 * 16000), samplerate=16000, channels=1)
sd.wait()
print('Recorded!')
"
```

### Whisper Too Slow

**Solutions:**
1. Use smaller model: Change `"whisper_model": "tiny"` in voice_config.json
2. Use whisper.cpp (C++ implementation, much faster)
3. Use GPU if available

### Background Noise Issues

**Solutions:**
1. Increase `silence_threshold` in voice_config.json
2. Use better microphone
3. Enable noise suppression in OBS
4. Use push-to-talk mode instead

---

## 🎓 Best Practices

### During Problem Solving:

**Do:**
- ✅ Think aloud constantly
- ✅ Explain your reasoning
- ✅ Ask questions verbally
- ✅ Respond to my probing questions
- ✅ Mention edge cases as you think of them

**Don't:**
- ❌ Code silently for long periods
- ❌ Ignore my questions
- ❌ Forget you're in interview mode
- ❌ Get frustrated with questions (they're valuable practice!)

### Communication Tips:

```
Good: "I'm using a hash map because I need O of 1 lookup to avoid
       the O of n squared brute force approach."

Better: "Let me think through the approaches. Brute force would be
         nested loops checking all pairs - that's O of n squared.
         I can optimize with a hash map for O of 1 lookups, making
         it O of n overall. The trade-off is O of n space."
```

---

## 🔧 Advanced Usage

### Manual Control During Session

```bash
# Start interactive mode
./.claude/hooks/interactive_mode.py start

# Stop it (or say "Claude, pause")
./.claude/hooks/interactive_mode.py stop

# Check if running
./.claude/hooks/interactive_mode.py status
```

### Record and Transcribe Without Interactive Mode

```bash
# Just get transcription
./.claude/hooks/utils/voice_detector.py
# Speak... wait for silence... get text output
```

---

## 📊 What Gets Tracked

The interactive mode logs:
- All your spoken statements
- All my responses
- Timestamps
- Silence duration
- Communication frequency

This data is used to score your **communication effectiveness** during evaluation!

---

## 🎉 You're Ready!

Your system is now fully voice-interactive.

**To start your first voice interview:**

1. Open terminal in `/home/badong/Projects/learning-dsa/`
2. Say or type: `/start-session 1 1`
3. Watch the video
4. Say: "Claude, I watched the video"
5. Complete quiz verbally
6. Say: "Give me the problem"
7. Start interactive mode: `./.claude/hooks/interactive_mode.py start`
8. **Think aloud while coding!**
9. Natural conversation with me
10. Say: "I'm done coding"
11. Verbal testing and evaluation

---

**Ready to start your first voice-interactive interview?** 🎤🚀

[Back to README](./README.md)
