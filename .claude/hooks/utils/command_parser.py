#!/home/badong/Projects/learning-dsa/whisper-env/bin/python3
"""
Voice Command Parser

Parses natural language commands and maps them to slash commands.
Handles variations and extracts parameters.

Example:
    "Claude start session 1 1" → /start-session 1 1
    "give me the problem" → /problem
    "I'm stuck" → /hint
"""

import re
from typing import Optional, Tuple

class CommandParser:
    def __init__(self):
        # Command patterns with regex
        self.patterns = [
            # Session management
            (r'(?:claude,?\s*)?start\s+session\s+(\d+)\s+(\d+)', lambda m: f"/start-session {m.group(1)} {m.group(2)}"),
            (r'(?:claude,?\s*)?resume', lambda m: "/resume"),
            (r'(?:claude,?\s*)?next\s+session', lambda m: "/next-session"),
            (r'(?:claude,?\s*)?end\s+session', lambda m: "/end-session"),

            # Interview flow
            (r'(?:claude,?\s*)?(?:i\s+)?watched\s+(?:the\s+)?video', lambda m: "/quiz-me"),
            (r'(?:claude,?\s*)?quiz\s+me', lambda m: "/quiz-me"),
            (r'(?:claude,?\s*)?(?:give\s+me\s+)?(?:the\s+)?problem', lambda m: "/problem"),
            (r'^go$', lambda m: "/problem"),
            (r'(?:claude,?\s*)?give\s+me\s+tips?', lambda m: "I'll share tips for this topic."),
            (r'(?:claude,?\s*)?start\s+timer', lambda m: "Timer started!"),
            (r'(?:claude,?\s*)?(?:i'm\s+)?done\s+coding', lambda m: "Good! Now walk me through your solution."),

            # Help & Hints
            (r'(?:claude,?\s*)?(?:i'm\s+)?stuck', lambda m: "/hint"),
            (r'(?:claude,?\s*)?(?:give\s+me\s+a\s+)?hint', lambda m: "/hint"),
            (r'(?:claude,?\s*)?another\s+hint', lambda m: "Providing stronger hint..."),
            (r'(?:claude,?\s*)?(?:i\s+)?(?:really\s+)?need\s+help', lambda m: "Providing detailed hint..."),
            (r'(?:claude,?\s*)?show\s+(?:me\s+)?(?:the\s+)?solution', lambda m: "Showing solution (marking for review)..."),
            (r'^help$', lambda m: "/hint"),

            # Evaluation
            (r'(?:claude,?\s*)?evaluate\s+me', lambda m: "/evaluate"),
            (r'(?:claude,?\s*)?(?:how\s+did\s+i\s+do|what\s+did\s+i\s+miss)', lambda m: "/evaluate"),
            (r'(?:claude,?\s*)?is\s+my\s+complexity\s+right', lambda m: "Let me verify your complexity analysis..."),
            (r'(?:claude,?\s*)?can\s+i\s+optimize', lambda m: "Let me suggest optimizations..."),

            # Progress
            (r'(?:claude,?\s*)?(?:my\s+)?(?:progress|stats)', lambda m: "/my-stats"),
            (r'(?:claude,?\s*)?mark\s+(?:as\s+)?complete', lambda m: "/mark-complete"),
            (r'(?:claude,?\s*)?(?:what's\s+)?next(?:\s+problem)?', lambda m: "Moving to next problem..."),
            (r'^next$', lambda m: "Moving to next problem..."),
            (r'(?:claude,?\s*)?save\s+(?:my\s+)?work', lambda m: "Saving your progress..."),
            (r'^stats$', lambda m: "/my-stats"),

            # Quick reference
            (r'(?:claude,?\s*)?show\s+pattern\s+(.+)', lambda m: f"Showing pattern: {m.group(1)}"),
            (r'(?:claude,?\s*)?typescript\s+(.+)', lambda m: f"Showing TypeScript reference for: {m.group(1)}"),
            (r'(?:claude,?\s*)?what\s+pattern\s+is\s+this', lambda m: "Let me help identify the pattern..."),

            # Time management
            (r'(?:claude,?\s*)?(?:time\s+check|how\s+much\s+time)', lambda m: "Checking time..."),
            (r'(?:claude,?\s*)?pause\s+timer', lambda m: "Timer paused."),
            (r'^time$', lambda m: "Checking time..."),
        ]

    def parse(self, text: str) -> Tuple[Optional[str], bool]:
        """
        Parse natural language into command or response.

        Returns:
            (command_or_response, is_slash_command)

        Example:
            ("start-session 1 1", True) → Execute /start-session 1 1
            ("Showing pattern: two pointers", False) → Just respond with text
            (None, False) → Not a command, pass through
        """
        text_lower = text.lower().strip()

        # Try each pattern
        for pattern, handler in self.patterns:
            match = re.search(pattern, text_lower)
            if match:
                result = handler(match)

                # Check if it's a slash command
                is_slash_command = result.startswith('/')

                return result, is_slash_command

        # Not a recognized command
        return None, False

    def extract_parameters(self, text: str, command_type: str) -> dict:
        """
        Extract parameters from natural language for specific commands.

        Example:
            text: "Claude, start session 2 3"
            command_type: "start-session"
            returns: {"day": 2, "session": 3}
        """
        params = {}

        if command_type == "start-session":
            match = re.search(r'session\s+(\d+)\s+(\d+)', text.lower())
            if match:
                params['day'] = int(match.group(1))
                params['session'] = int(match.group(2))

        return params

# Test function
def test_parser():
    """Test command parser with examples"""
    parser = CommandParser()

    test_cases = [
        "Claude, start session 1 1",
        "give me the problem",
        "I'm stuck",
        "give me a hint",
        "I'm done coding",
        "evaluate me",
        "next problem",
        "my progress",
        "show pattern two pointers",
    ]

    print("Testing Command Parser:")
    print("=" * 60)

    for test in test_cases:
        result, is_cmd = parser.parse(test)
        cmd_type = "SLASH COMMAND" if is_cmd else "RESPONSE"
        print(f"Input:  {test}")
        print(f"Output: {result} ({cmd_type})")
        print()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test_parser()
    else:
        # Parse stdin
        parser = CommandParser()
        text = sys.stdin.read().strip()
        result, is_slash_cmd = parser.parse(text)

        if result:
            print(json.dumps({
                "command": result,
                "is_slash_command": is_slash_cmd
            }))
        else:
            print(json.dumps({
                "command": None,
                "is_slash_command": False
            }))
