class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # The robot returns to the origin if:
        # 1. Total 'U' moves == Total 'D' moves
        # 2. Total 'L' moves == Total 'R' moves
        
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')