from collections import deque

class Solution:
    def minJumps(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        max_val = max(nums)
        
        # Sieve to find smallest prime factor (SPF) for all numbers up to max_val
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:
                for j in range(i*i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        
        # Pre-compute which indices contain multiples of which primes
        prime_to_indices = {}
        for i, val in enumerate(nums):
            temp = val
            visited_factors = set()
            while temp > 1:
                p = spf[temp]
                if p not in visited_factors:
                    if p not in prime_to_indices:
                        prime_to_indices[p] = []
                    prime_to_indices[p].append(i)
                    visited_factors.add(p)
                temp //= p

        # BFS Setup
        queue = deque([(0, 0)]) # (index, distance)
        visited_indices = {0}
        visited_primes = set()
        
        # Quick check for primality
        def is_prime(num):
            if num < 2: return False
            return spf[num] == num

        while queue:
            curr_idx, dist = queue.popleft()
            
            if curr_idx == n - 1:
                return dist
            
            # 1. Adjacent Step: i + 1, i - 1
            for neighbor in [curr_idx - 1, curr_idx + 1]:
                if 0 <= neighbor < n and neighbor not in visited_indices:
                    visited_indices.add(neighbor)
                    queue.append((neighbor, dist + 1))
            
            # 2. Prime Teleportation: If nums[i] is prime p, jump to all multiples of p
            val = nums[curr_idx]
            if is_prime(val):
                p = val
                if p not in visited_primes:
                    visited_primes.add(p)
                    if p in prime_to_indices:
                        for target_idx in prime_to_indices[p]:
                            if target_idx not in visited_indices:
                                visited_indices.add(target_idx)
                                queue.append((target_idx, dist + 1))
                                
        return -1
        