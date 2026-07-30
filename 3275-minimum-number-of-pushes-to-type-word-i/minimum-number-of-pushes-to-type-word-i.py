class Solution:

    def minimumPushes(self, word: str) -> int:
        n = len(word)
        pushes = 0

        # We have 8 keys available (keys 2 through 9).
        # We greedily fill each key with 1 letter first, then 2, then 3, etc.
        for i in range(n):
            cost = (i // 8) + 1
            pushes += cost

        return pushes