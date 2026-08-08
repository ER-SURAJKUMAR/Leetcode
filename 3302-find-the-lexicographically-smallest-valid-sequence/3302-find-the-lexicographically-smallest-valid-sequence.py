class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        m, n = len(word1), len(word2)
        
        # last[j] stores the largest index in word1 from which 
        # the suffix word2[j...] can be matched EXACTLY.
        last = [-1] * (n + 1)
        last[n] = m
        
        p = m - 1
        for j in range(n - 1, -1, -1):
            while p >= 0 and word1[p] != word2[j]:
                p -= 1
            last[j] = p
            if p >= 0:
                p -= 1
                
        ans = []
        i = 0
        changed = False
        
        for j in range(n):
            if not changed:
                # If we can afford a mismatch at j (or an exact match),
                # pick index i immediately to minimize index value.
                if i + 1 <= last[j + 1]:
                    if word1[i] != word2[j]:
                        changed = True
                    ans.append(i)
                    i += 1
                else:
                    # Must find an exact match for word2[j]
                    while i < m and word1[i] != word2[j]:
                        i += 1
                    if i >= m:
                        return []
                    ans.append(i)
                    i += 1
            else:
                # Mismatch already used; must match exactly
                while i < m and word1[i] != word2[j]:
                    i += 1
                if i >= m or i + 1 > last[j + 1]:
                    return []
                ans.append(i)
                i += 1
                
        return ans if len(ans) == n else []