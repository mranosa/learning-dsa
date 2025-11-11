#!/usr/bin/env python3
"""
Voice Activity Detection (VAD) System

Continuously monitors microphone for speech, records audio,
and transcribes with Whisper for hands-free interaction.
"""

import sys
import os
import json
import time
import tempfile
from pathlib import Path
import sounddevice as sd
import numpy as np
import whisper

# Configuration
CONFIG_FILE = Path(__file__).parent / "voice_config.json"

DEFAULT_CONFIG = {
    "whisper_model": "base",      # tiny, base, small, medium, large
    "language": "en",              # Or "auto" for auto-detect
    "sample_rate": 16000,          # Whisper expects 16kHz
    "silence_threshold": 0.01,     # RMS amplitude threshold
    "silence_duration": 1.5,       # Seconds of silence to stop recording
    "min_recording_duration": 0.5, # Minimum seconds to consider valid
    "max_recording_duration": 30,  # Maximum seconds per recording
}

class VoiceDetector:
    def __init__(self):
        # Load configuration
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE) as f:
                config = json.load(f)
            self.config = {**DEFAULT_CONFIG, **config}
        else:
            self.config = DEFAULT_CONFIG
            # Save default config
            with open(CONFIG_FILE, 'w') as f:
                json.dump(DEFAULT_CONFIG, f, indent=2)

        # Load Whisper model
        print(f"Loading Whisper model '{self.config['whisper_model']}'...", file=sys.stderr)
        self.model = whisper.load_model(self.config['whisper_model'])
        print("✅ Whisper model loaded", file=sys.stderr)

        # Audio recording state
        self.is_recording = False
        self.audio_data = []
        self.silence_start = None

    def calculate_rms(self, audio_chunk):
        """Calculate RMS (Root Mean Square) amplitude"""
        return np.sqrt(np.mean(audio_chunk**2))

    def record_until_silence(self):
        """
        Records audio until silence is detected.
        Returns path to temporary audio file.
        """
        print("🎤 Listening... (speak now)", file=sys.stderr)

        self.audio_data = []
        self.silence_start = None
        recording_start = time.time()

        def audio_callback(indata, frames, time_info, status):
            """Called for each audio block"""
            if status:
                print(f"Status: {status}", file=sys.stderr)

            # Calculate volume (RMS)
            volume = self.calculate_rms(indata)

            # Check if speech detected (above threshold)
            if volume > self.config['silence_threshold']:
                self.audio_data.append(indata.copy())
                self.silence_start = None  # Reset silence timer
            else:
                # Silence detected
                if len(self.audio_data) > 0:  # Only count silence if we've recorded something
                    if self.silence_start is None:
                        self.silence_start = time.time()

        # Start recording
        with sd.InputStream(
            callback=audio_callback,
            channels=1,
            samplerate=self.config['sample_rate'],
            dtype=np.float32
        ):
            while True:
                time.sleep(0.1)  # Check every 100ms

                # Stop conditions
                recording_duration = time.time() - recording_start

                # Max duration reached
                if recording_duration > self.config['max_recording_duration']:
                    print("⏱️  Max duration reached", file=sys.stderr)
                    break

                # Silence detected for configured duration
                if self.silence_start and (time.time() - self.silence_start) > self.config['silence_duration']:
                    print("🔇 Silence detected, processing...", file=sys.stderr)
                    break

        # Check if we recorded enough
        if recording_duration < self.config['min_recording_duration']:
            print("⚠️  Recording too short, ignoring", file=sys.stderr)
            return None

        if len(self.audio_data) == 0:
            print("⚠️  No audio detected", file=sys.stderr)
            return None

        # Concatenate all audio chunks
        audio_array = np.concatenate(self.audio_data, axis=0)

        # Save to temporary file
        temp_file = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
        temp_path = temp_file.name
        temp_file.close()

        # Save as WAV using sounddevice
        sd.write(temp_path, audio_array, self.config['sample_rate'])

        print(f"✅ Audio saved ({recording_duration:.1f}s)", file=sys.stderr)
        return temp_path

    def transcribe(self, audio_path):
        """Transcribe audio file with Whisper"""
        print("🔄 Transcribing...", file=sys.stderr)

        # Transcribe with Whisper
        result = self.model.transcribe(
            audio_path,
            language=self.config['language'] if self.config['language'] != 'auto' else None,
            fp16=False  # Use FP32 for CPU
        )

        text = result['text'].strip()

        # Clean up temp file
        try:
            os.unlink(audio_path)
        except:
            pass

        return text

    def listen_once(self):
        """
        Listen for one utterance, transcribe it, and return the text.
        Returns None if no speech detected.
        """
        audio_path = self.record_until_silence()

        if not audio_path:
            return None

        text = self.transcribe(audio_path)
        print(f"✅ Transcribed: {text}", file=sys.stderr)

        return text

def main():
    """
    Main entry point for voice detection.
    Listens for one utterance and outputs transcribed text.
    """
    try:
        detector = VoiceDetector()
        text = detector.listen_once()

        if text:
            # Output transcribed text to stdout
            print(text)
        else:
            print("", file=sys.stderr)

    except KeyboardInterrupt:
        print("\n🛑 Stopped by user", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
