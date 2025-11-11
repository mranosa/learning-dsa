#!/home/badong/Projects/learning-dsa/whisper-env/bin/python3
"""
Interactive Coding Mode - Real-time voice conversation during problem-solving

This enables continuous voice interaction where:
- User thinks aloud while coding
- Claude responds in real-time
- Interview-style probing questions
- Natural back-and-forth conversation

Usage:
    ./interactive_mode.py start    # Start interactive mode
    ./interactive_mode.py stop     # Stop interactive mode
    ./interactive_mode.py status   # Check if running
"""

import sys
import os
import json
import time
import subprocess
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
STATE_FILE = SCRIPT_DIR / '..' / 'SESSION-STATE.json'
INTERACTIVE_STATE_FILE = SCRIPT_DIR / 'utils' / 'interactive_state.json'

class InteractiveMode:
    def __init__(self):
        self.load_state()
        self.last_speech_time = None
        self.silence_warnings_given = 0

    def load_state(self):
        """Load session state to understand context"""
        if STATE_FILE.exists():
            with open(STATE_FILE) as f:
                self.session_state = json.load(f)
        else:
            self.session_state = {}

        # Load interactive state
        if INTERACTIVE_STATE_FILE.exists():
            with open(INTERACTIVE_STATE_FILE) as f:
                self.interactive_state = json.load(f)
        else:
            self.interactive_state = {
                "active": False,
                "mode": "coding",  # coding, testing, evaluation
                "start_time": None,
                "user_statements": [],
                "claude_responses": [],
                "silence_count": 0
            }

    def save_interactive_state(self):
        """Save interactive state"""
        INTERACTIVE_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(INTERACTIVE_STATE_FILE, 'w') as f:
            json.dump(self.interactive_state, f, indent=2)

    def is_question(self, text):
        """Detect if statement is a question"""
        question_words = ['what', 'why', 'how', 'when', 'where', 'which', 'who', 'can', 'should', 'would', 'could', 'is', 'are', 'do', 'does']
        text_lower = text.lower().strip()

        # Ends with question mark
        if text_lower.endswith('?'):
            return True

        # Starts with question word
        for word in question_words:
            if text_lower.startswith(word + ' '):
                return True

        return False

    def is_command(self, text):
        """Detect if statement is a voice command"""
        commands = ['give me', 'show me', 'next', 'hint', 'stuck', 'done', 'evaluate', 'help', 'start', 'resume']
        text_lower = text.lower().strip()

        for cmd in commands:
            if cmd in text_lower:
                return True

        return False

    def is_thinking_aloud(self, text):
        """Detect if user is thinking aloud (not asking question)"""
        thinking_phrases = [
            "i think", "i'll", "i'm", "let me", "i should", "i need to",
            "creating", "using", "looping", "checking", "adding",
            "this will", "this should", "so i", "now i"
        ]

        text_lower = text.lower().strip()

        for phrase in thinking_phrases:
            if phrase in text_lower:
                return True

        return False

    def generate_response(self, text):
        """
        Generate appropriate interviewer response based on what user said.

        Returns:
            (response_text, should_wait_for_user_response)
        """
        # Command - let command system handle it
        if self.is_command(text):
            return None, False  # Command parser will handle

        # Question - answer it
        if self.is_question(text):
            # These will be context-specific, but provide general responses
            if 'complexity' in text.lower():
                return "Think about how many operations you're doing. Are you looping? How many times?", True
            elif 'edge case' in text.lower():
                return "Good thinking! Consider empty input, single element, and maximum constraints.", True
            elif 'empty' in text.lower() or 'null' in text.lower():
                return "Excellent edge case to consider! How would your code handle that?", True
            else:
                return "That's a good question. What are your thoughts?", True

        # Thinking aloud - brief acknowledgment or probing question
        if self.is_thinking_aloud(text):
            # Occasionally probe (not every statement)
            if 'hash map' in text.lower() or 'map' in text.lower():
                return "Good choice. What's the time complexity of that approach?", False
            elif 'loop' in text.lower():
                return "How many times will that loop run?", False
            elif 'creating' in text.lower() or 'using' in text.lower():
                return "Sounds good. Keep going.", False
            else:
                return "Mm-hmm.", False  # Brief acknowledgment

        # Statement/observation - acknowledge
        return "I see. Continue.", False

    def speak(self, text):
        """Use TTS to speak a response"""
        try:
            tts_script = SCRIPT_DIR / 'elevenlabs_tts.py'
            env = os.environ.copy()
            env['TTS_SILENT_MODE'] = 'true'

            subprocess.run(
                [str(tts_script), text],
                env=env,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except Exception as e:
            print(f"TTS error: {e}", file=sys.stderr)

    def listen_and_respond_loop(self):
        """
        Continuous listen loop during coding phase.
        Listens for user speech, generates responses, maintains conversation.
        """
        print("\n" + "="*60, file=sys.stderr)
        print("🎤 INTERACTIVE CODING MODE ACTIVE", file=sys.stderr)
        print("="*60, file=sys.stderr)
        print("Speak naturally while coding. I'll listen and respond.", file=sys.stderr)
        print("Say 'Claude, pause' to stop listening.", file=sys.stderr)
        print("Say 'Claude, I'm done coding' when finished.", file=sys.stderr)
        print("="*60 + "\n", file=sys.stderr)

        # Import voice detector
        sys.path.insert(0, str(SCRIPT_DIR / 'utils'))
        from voice_detector import VoiceDetector

        detector = VoiceDetector()

        while self.interactive_state['active']:
            # Listen for user speech
            user_text = detector.listen_once()

            if not user_text:
                # Check silence duration
                if self.last_speech_time:
                    silence_duration = time.time() - self.last_speech_time

                    # After 30s of silence, check in
                    if silence_duration > 30 and self.silence_warnings_given == 0:
                        self.speak("You've been quiet for a bit. Can you talk me through what you're thinking?")
                        self.silence_warnings_given += 1

                    # After 60s, more direct
                    elif silence_duration > 60 and self.silence_warnings_given == 1:
                        self.speak("Still working? What's blocking you?")
                        self.silence_warnings_given += 2

                continue

            # Reset silence tracking
            self.last_speech_time = time.time()
            self.silence_warnings_given = 0

            # Log user statement
            self.interactive_state['user_statements'].append({
                "text": user_text,
                "timestamp": datetime.now().isoformat()
            })

            # Display transcription
            print(f"\n[You]: {user_text}", file=sys.stderr)

            # Check for stop commands
            if 'pause' in user_text.lower() or 'stop listening' in user_text.lower():
                self.speak("Pausing interactive mode.")
                self.interactive_state['active'] = False
                self.save_interactive_state()
                break

            if "i'm done" in user_text.lower() or "done coding" in user_text.lower():
                self.speak("Great! Let's test your solution. Say 'Claude, evaluate me' when ready.")
                # Could auto-trigger evaluation here
                continue

            # Generate response
            response_text, wait_for_response = self.generate_response(user_text)

            if response_text:
                # Display and speak response
                print(f"[Claude]: {response_text}", file=sys.stderr)
                self.speak(response_text)

                # Log response
                self.interactive_state['claude_responses'].append({
                    "text": response_text,
                    "timestamp": datetime.now().isoformat(),
                    "in_response_to": user_text
                })

                self.save_interactive_state()

                # If asked a question, wait a bit for their response
                if wait_for_response:
                    time.sleep(0.5)

def main():
    if len(sys.argv) < 2:
        print("Usage: ./interactive_mode.py [start|stop|status]")
        sys.exit(1)

    command = sys.argv[1].lower()
    mode = InteractiveMode()

    if command == 'start':
        mode.interactive_state['active'] = True
        mode.interactive_state['start_time'] = datetime.now().isoformat()
        mode.interactive_state['user_statements'] = []
        mode.interactive_state['claude_responses'] = []
        mode.save_interactive_state()

        print("🎙️  Starting interactive coding mode...", file=sys.stderr)
        mode.listen_and_respond_loop()

    elif command == 'stop':
        mode.interactive_state['active'] = False
        mode.save_interactive_state()
        print("🛑 Interactive mode stopped", file=sys.stderr)

    elif command == 'status':
        if mode.interactive_state.get('active', False):
            print("✅ Interactive mode is ACTIVE")
        else:
            print("⭕ Interactive mode is OFF")

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == '__main__':
    main()
