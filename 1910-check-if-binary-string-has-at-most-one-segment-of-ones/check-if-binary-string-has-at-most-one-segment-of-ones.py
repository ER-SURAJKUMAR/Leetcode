class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # Since s[0] is always '1', a second segment of '1's 
        # can only exist if "01" is present in the string.
        return "01" not in s