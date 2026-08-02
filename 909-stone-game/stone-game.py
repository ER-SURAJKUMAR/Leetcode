class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        # Alice can always force a win by choosing either all odd or all even indexed piles
        return True