class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        OFFSET = n + 1
        bit = [0] * (2 * n + 5)
        
        def update(idx: int, val: int):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx: int) -> int:
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s

        update(0 + OFFSET, 1)
        
        current_sum = 0
        total_subarrays = 0
        
        for num in nums:
            if num == target:
                current_sum += 1
            else:
                current_sum -= 1
            
            total_subarrays += query(current_sum + OFFSET - 1)
            update(current_sum + OFFSET, 1)
            
        return total_subarrays