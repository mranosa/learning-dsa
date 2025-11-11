#!/usr/bin/env python3
"""
Update Claude Code status line with learning progress.
Shows both session and overall progress.
"""

import json
import sys
import os
from pathlib import Path

# Get project root (3 levels up from this script)
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
SESSION_STATE_FILE = PROJECT_ROOT / "SESSION-STATE.json"

# Total sessions and problems
TOTAL_DAYS = 7
TOTAL_SESSIONS = 21
TOTAL_PROBLEMS = 120

def load_session_state():
    """Load current session state."""
    if not SESSION_STATE_FILE.exists():
        return None

    try:
        with open(SESSION_STATE_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading session state: {e}", file=sys.stderr)
        return None

def calculate_session_number(day, session):
    """Calculate overall session number from day and session."""
    # Day 1, Session 1 = Session 1
    # Day 1, Session 2 = Session 2
    # Day 2, Session 1 = Session 4, etc.
    return (day - 1) * 3 + session

def generate_status_line(state):
    """Generate status line text from session state."""
    if not state:
        return "DSA Bootcamp - Ready to start!"

    day = state.get("currentDay", 1)
    session_in_day = state.get("currentSession", 1)
    session_number = calculate_session_number(day, session_in_day)
    topic = state.get("sessionTopic", "Unknown")
    problem_index = state.get("currentProblemIndex", 0)
    problems_in_session = state.get("totalProblemsInSession", 10)
    total_completed = state.get("totalProblemsCompleted", 0)
    phase = state.get("phase", "not-started")

    # Format: "Day 2/7 | Session 2/21: Hash Maps | Problem 3/10 | 15/120 total"
    parts = []

    # Day progress
    parts.append(f"Day {day}/{TOTAL_DAYS}")

    # Session progress with topic
    parts.append(f"Session {session_number}/{TOTAL_SESSIONS}: {topic}")

    # Current problem (only if session started)
    if phase != "not-started" and problem_index > 0:
        parts.append(f"Problem {problem_index}/{problems_in_session}")

    # Total progress
    parts.append(f"{total_completed}/{TOTAL_PROBLEMS} solved")

    return " | ".join(parts)

def main():
    """Main entry point."""
    state = load_session_state()
    status_line = generate_status_line(state)
    print(status_line)

if __name__ == "__main__":
    main()
