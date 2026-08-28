from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        # Check if s can form a palindrome
        odd_chars = [char for char, count in counts.items() if count % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid = odd_chars[0] if odd_chars else ""
        
        # Half counts for the first half of the palindrome
        half_counts = {char: count // 2 for char, count in counts.items()}
        m = n // 2

        def build_palindrome(half_str: str) -> str:
            if n % 2 == 1:
                return half_str + mid + half_str[::-1]
            return half_str + half_str[::-1]

        # Search for the lexicographically smallest half-string
        def search(idx: int, current_half: list, available: dict, is_greater: bool) -> str:
            if idx == m:
                res = build_palindrome("".join(current_half))
                return res if res > target else ""

            t_char = target[idx]
            sorted_chars = sorted(available.keys())
            
            for ch in sorted_chars:
                if available[ch] == 0:
                    continue
                
                if not is_greater and ch < t_char:
                    continue
                
                available[ch] -= 1
                current_half.append(ch)
                
                next_is_greater = is_greater or (ch > t_char)
                res = search(idx + 1, current_half, available, next_is_greater)
                if res:
                    return res
                
                current_half.pop()
                available[ch] += 1
            
            return ""

        return search(0, [], half_counts, False)