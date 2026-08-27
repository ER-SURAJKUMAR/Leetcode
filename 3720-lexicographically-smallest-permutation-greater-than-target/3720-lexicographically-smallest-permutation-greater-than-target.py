from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_counts = Counter(s)
        prefix_counts = Counter()
        
        # Build initial prefix counts for the full target length
        for i in range(n):
            prefix_counts[target[i]] += 1
        
        def can_form_prefix(p_counts):
            return all(total_counts[char] >= p_counts[char] for char in p_counts)

        # Iterate point of divergence i from n-1 down to 0
        for i in range(n - 1, -1, -1):
            # Exclude target[i] from prefix since index i will differ
            prefix_counts[target[i]] -= 1
            if prefix_counts[target[i]] == 0:
                del prefix_counts[target[i]]
            
            # Check if target[:i] can be formed by available characters
            if not can_form_prefix(prefix_counts):
                continue
            
            # Remaining characters available after forming target[:i]
            avail = total_counts - prefix_counts
            
            # Find the smallest character strictly greater than target[i]
            target_char = target[i]
            larger_char = None
            for char in sorted(avail.keys()):
                if char > target_char and avail[char] > 0:
                    larger_char = char
                    break
            
            # Construct the smallest lexicographical valid result
            if larger_char:
                res = list(target[:i]) + [larger_char]
                avail[larger_char] -= 1
                
                # Append all remaining characters in ascending order
                for char in sorted(avail.keys()):
                    res.extend([char] * avail[char])
                
                return "".join(res)
        
        return ""