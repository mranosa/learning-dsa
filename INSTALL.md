# Installation & Setup Guide

Complete first-time setup for the Interactive Voice Interview Bootcamp.

---

## Prerequisites

- Linux system (tested on Ubuntu)
- Python 3.8+
- Node.js (for running TypeScript - optional)
- Microphone
- Speakers/headphones
- ElevenLabs API key

---

## Step-by-Step Setup

### 1. Install System Dependencies

```bash
# Keyboard automation (for F12 voice input)
sudo apt-get update
sudo apt-get install -y xdotool xbindkeys

# Audio tools (if not already installed)
sudo apt-get install -y pulseaudio portaudio19-dev
```

---

### 2. Set Up Python Environment

**Whisper is already installed in whisper-env!**

Verify:
```bash
whisper-env/bin/python3 -c "import whisper; print('✅ Whisper ready!')"
```

If not installed:
```bash
whisper-env/bin/pip install openai-whisper sounddevice numpy
```

---

### 3. Configure ElevenLabs TTS

**Create `.env` file** (if not exists):
```bash
# In project root
echo "ELEVENLABS_API_KEY=your_api_key_here" > .env
```

**Get API key:**
1. Sign up at https://elevenlabs.io
2. Go to Profile → API Keys
3. Copy your key
4. Paste in .env

**Test TTS:**
```bash
./.claude/hooks/elevenlabs_tts.py "Testing my Badong voice"
```

Should hear audio!

---

### 4. Verify Installation

```bash
./system-check
```

**Expected output:**
```
✅ TTS (ElevenLabs): Configured
✅ Whisper (STT): Installed
✅ xdotool (F12): Installed
✅ xbindkeys (Hotkeys): Installed but not running
✅ Voice scripts: All present
✅ Session 1 files: Ready
✅ Printables: All created
✅ Vocabulary guides: Both ready

ALL SYSTEMS GO!
```

---

### 5. Activate Voice System

```bash
# Activate F12 hotkey
./setup-voice-hotkeys

# Should see:
# ✅ Voice hotkeys activated!
# F12 → Voice input
```

---

### 6. Run Session 0 (Test Session)

**Recommended before starting real sessions!**

```bash
# Start interactive mode
./voice-interview
```

Then **press F12** and say:
```
"Claude, start session 0 0, ok submit"
```

Complete the 3 test problems (~20 min)

---

## Workspace Setup

### Browser:
- **Tab 1:** Learning materials (videos, docs)
- **Tab 2:** LeetCode.com

### Terminal:
- Run Claude Code CLI
- Run `./setup-voice-hotkeys && ./voice-interview`

**That's it!** No need for multiple terminals.

---

## First Session Checklist

Before starting Session 1:

- [ ] Ran `./system-check` - all ✅
- [ ] Completed Session 0 (test session)
- [ ] F12 works from LeetCode
- [ ] Voice responses clear
- [ ] Interactive mode works
- [ ] Printed quick-reference cards
- [ ] Vocabulary guides accessible

---

## Quick Start

**Every session, just run:**
```bash
cd /home/badong/Projects/learning-dsa
./setup-voice-hotkeys && ./voice-interview
```

**Then F12:**
```
"Claude, start session [day] [number], ok submit"
```

**That's it!**

---

## Troubleshooting

### TTS Not Working
```bash
# Check API key
grep ELEVENLABS_API_KEY .env

# Test directly
./.claude/hooks/elevenlabs_tts.py "test"
```

### Whisper Not Working
```bash
# Test import
whisper-env/bin/python3 -c "import whisper"

# If fails, reinstall
whisper-env/bin/pip install --upgrade openai-whisper
```

### F12 Not Working
```bash
# Check if xbindkeys running
pgrep xbindkeys

# If not, restart
./setup-voice-hotkeys

# Test xdotool
xdotool search --name "claude"
```

### Interactive Mode Not Responding
```bash
# Make sure it's running
./voice-interview status

# Restart if needed
./voice-interview stop
./voice-interview start
```

---

## Optional: Streaming Setup

See [STREAMING-TIPS.md](./STREAMING-TIPS.md) for:
- OBS configuration
- Screen layout
- Overlays
- Audio routing

---

## File Structure Reference

```
learning-dsa/
├── system-check          ← Run this first
├── setup-voice-hotkeys   ← Activate F12
├── voice-interview       ← Start interactive mode
├── README.md             ← Master navigation
├── INSTALL.md            ← You are here
├── VOICE-SETUP.md        ← Detailed voice guide
├── THINKING-ALOUD-PHRASES.md  ← Communication help
├── TECHNICAL-VOCABULARY.md    ← Term definitions
└── day-0/session-0-system-test/  ← Test session
```

---

## Getting Help

**Documentation:**
- VOICE-SETUP.md - Voice system details
- COMMAND-GUIDE.md - All commands explained
- SESSION-FLOW.md - How sessions work
- QUICK-START-CARD.md - One-page reference

**Commands:**
```bash
./system-check          # Verify system
./voice-interview test  # Test voice only
```

---

## You're Ready!

**Run Session 0 to test, then start Session 1!**

```bash
./setup-voice-hotkeys && ./voice-interview
```

**F12:** "Claude, start session 0 0, ok submit"

Good luck! 🚀
