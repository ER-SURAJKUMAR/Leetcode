from collections import Counter
import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = Counter(s)
        
        # Extract half counts and middle character
        half_counts = [0] * 26
        mid = ""
        
        for char, cnt in counts.items():
            idx = ord(char) - ord('a')
            if cnt % 2 == 1:
                mid = char
            half_counts[idx] = cnt // 2
            
        total_half_len = sum(half_counts)
        MAX_K = k + 1
        
        # Calculate distinct permutations capped at MAX_K
        def count_permutations(freq_list):
            total = sum(freq_list)
            res = 1
            for freq in freq_list:
                if freq > 0:
                    res *= math.comb(total, freq)
                    total -= freq
                    if res >= MAX_K:
                        return MAX_K
            return res

        # Check total possible permutations
        if count_permutations(half_counts) < k:
            return ""

        left_half = []

        for _ in range(total_half_len):
            for i in range(26):
                if half_counts[i] == 0:
                    continue
                
                # Try placing character `i`
                half_counts[i] -= 1
                perms = count_permutations(half_counts)
                
                if k <= perms:
                    left_half.append(chr(ord('a') + i))
                    break
                else:
                    k -= perms
                    half_counts[i] += 1  # Backtrack

        left_str = "".join(left_half)
        return left_str + mid + left_str[::-1]