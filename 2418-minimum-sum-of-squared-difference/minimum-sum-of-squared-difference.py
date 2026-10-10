class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diff = [abs(nums1[i] - nums2[i]) for i in range(n)]
        total_k = k1 + k2
        
        # If total budget is enough to reduce all differences to 0
        if sum(diff) <= total_k:
            return 0
        
        max_diff = max(diff)
        count = [0] * (max_diff + 1)
        for d in diff:
            count[d] += 1
            
        # Greedily reduce the largest differences
        for d in range(max_diff, 0, -1):
            if count[d] > 0:
                reduction = min(total_k, count[d])
                count[d] -= reduction
                count[d - 1] += reduction
                total_k -= reduction
                
                if total_k == 0:
                    break
                    
        # Calculate the final sum of squared differences
        ans = 0
        for d in range(max_diff + 1):
            if count[d] > 0:
                ans += count[d] * d * d
                
        return ans