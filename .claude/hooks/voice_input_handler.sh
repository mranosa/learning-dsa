#!/bin/bash
# F12 Voice Input Handler
# Press F12 → Speak → Auto-types into Claude Code → "ok submit" presses Enter
#
# Features:
# - Works from any window (targets Claude Code)
# - Detects "ok submit" / "okay submit" / "submit"
# - Auto-presses Enter if submit detected
# - Shows visual notifications
# - Handles errors gracefully

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Notification function
notify() {
    local title="$1"
    local message="$2"
    local urgency="${3:-normal}"

    if command -v notify-send &> /dev/null; then
        notify-send -u "$urgency" "$title" "$message"
    fi
    echo "[$title] $message" >&2
}

# Main voice input flow
main() {
    # Show recording notification
    notify "🎤 Voice Input" "Listening... Speak now!" "normal"

    # Record and transcribe using voice detector
    TEXT=$("$SCRIPT_DIR/utils/voice_detector.py" 2>/dev/null)

    # Check if transcription was successful
    if [ -z "$TEXT" ] || [ "$TEXT" == "" ]; then
        notify "⚠️ Voice Input" "No speech detected or transcription failed" "critical"
        exit 1
    fi

    # Show what was transcribed
    notify "✅ Transcribed" "$TEXT" "normal"

    # Check for "ok submit" / "okay submit" / "submit" command
    AUTO_SUBMIT=false
    if echo "$TEXT" | grep -qiE "(ok|okay)?\s*submit\s*$"; then
        AUTO_SUBMIT=true
        # Remove "ok submit" from the text
        TEXT=$(echo "$TEXT" | sed -E 's/,?\s*(ok|okay)?\s*submit\s*$//i')
        notify "⚡ Auto-Submit" "Will press Enter after typing" "normal"
    fi

    # Find Claude Code window
    # Try multiple patterns to find the window
    WINDOW_ID=$(xdotool search --name "claude" | head -1)

    if [ -z "$WINDOW_ID" ]; then
        # Try alternative patterns
        WINDOW_ID=$(xdotool search --class "claude" | head -1)
    fi

    if [ -z "$WINDOW_ID" ]; then
        # Try terminal with claude in title
        WINDOW_ID=$(xdotool search --name ".*claude.*" | head -1)
    fi

    if [ -z "$WINDOW_ID" ]; then
        notify "❌ Error" "Claude Code window not found. Make sure it's running." "critical"
        echo "Error: Could not find Claude Code window" >&2
        echo "Make sure Claude Code CLI is running in a terminal" >&2
        exit 1
    fi

    notify "🎯 Found Claude" "Window ID: $WINDOW_ID" "low"

    # Type the text into Claude Code window
    # Use --clearmodifiers to avoid interference from held keys
    # Type slowly to avoid missing characters
    xdotool type --window "$WINDOW_ID" --delay 10 --clearmodifiers "$TEXT"

    # Wait a moment for text to be typed
    sleep 0.2

    # Auto-press Enter if "ok submit" was detected
    if [ "$AUTO_SUBMIT" = true ]; then
        xdotool key --window "$WINDOW_ID" Return
        notify "✅ Submitted" "Command sent to Claude!" "normal"
    else
        notify "⌨️ Typed" "Press Enter to submit" "normal"
    fi
}

# Run main function
main "$@"
