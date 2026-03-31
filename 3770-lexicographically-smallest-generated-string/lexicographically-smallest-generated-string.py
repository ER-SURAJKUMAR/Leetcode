class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        sz = n + m - 1
        ans = [None] * sz
        modifiable = [True] * sz
        
        # 1. Handle all 'T' positions first.
        for i, tf in enumerate(str1):
            if tf == 'T':
                for j, c in enumerate(str2):
                    pos = i + j
                    if ans[pos] is not None and ans[pos] != c:
                        return ''
                    ans[pos] = c
                    modifiable[pos] = False
                    
        # 2. Fill all remaining positions with 'a'.
        for i in range(sz):
            if ans[i] is None:
                ans[i] = 'a'
                
        # 3. Handle all 'F' positions.
        # If an 'F' position matches str2, we must break it.
        # To keep it lexicographically smallest, we change the last modifiable 
        # character in that substring to 'b'.
        for i in range(n):
            if str1[i] == 'F':
                # Check if it matches str2
                match = True
                for j in range(m):
                    if ans[i + j] != str2[j]:
                        match = False
                        break
                
                if match:
                    # Find the last modifiable character in this range [i, i+m-1]
                    mod_pos = -1
                    for k in range(i + m - 1, i - 1, -1):
                        if modifiable[k]:
                            mod_pos = k
                            break
                            
                    if mod_pos == -1:
                        # No character can be changed to avoid matching str2
                        return ''
                        
                    ans[mod_pos] = 'b'
                    modifiable[mod_pos] = False
                    
        # Final check: Make sure we didn't accidentally break an earlier 'F' 
        # or create a new match that violates another constraint.
        for i in range(n):
            match = True
            for j in range(m):
                if ans[i + j] != str2[j]:
                    match = False
                    break
            
            if str1[i] == 'T' and not match:
                return ''
            if str1[i] == 'F' and match:
                return ''
                
        return "".join(ans)