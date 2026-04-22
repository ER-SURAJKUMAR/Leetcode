class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        result = []
        
        for q in queries:
            # Check this query against every word in the dictionary
            for d in dictionary:
                diff_count = 0
                # Compare characters at the same position
                for i in range(len(q)):
                    if q[i] != d[i]:
                        diff_count += 1
                    
                    # If differences exceed 2, this dictionary word won't work
                    if diff_count > 2:
                        break
                
                # If we found a match within 2 edits, add to result and stop checking dictionary
                if diff_count <= 2:
                    result.append(q)
                    break
                    
        return result