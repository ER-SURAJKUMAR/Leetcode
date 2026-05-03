class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # If lengths are different, s can never become goal
        if len(s) != len(goal):
            return False
        
        # If goal is a rotation of s, it must be a substring of s + s
        # For example: s = "abcde", s + s = "abcdeabcde"
        # All possible rotations ("bcdea", "cdeab", etc.) are contained within "abcdeabcde"
        return goal in (s + s)