import heapq
from collections import Counter

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        cost = [0] * (n - x + 1)
        
        lower_heap = []  # Max-heap (invert values)
        upper_heap = []  # Min-heap
        lower_sum = 0
        upper_sum = 0
        lower_size = 0
        upper_size = 0
        
        delayed = Counter()

        def clean_heap(heap, is_max_heap):
            while heap:
                val = -heap[0] if is_max_heap else heap[0]
                if delayed[val] > 0:
                    delayed[val] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def rebalance():
            nonlocal lower_sum, upper_sum, lower_size, upper_size
            
            clean_heap(lower_heap, True)
            clean_heap(upper_heap, False)
            
            if lower_size > upper_size + 1:
                clean_heap(lower_heap, True)
                val = -heapq.heappop(lower_heap)
                heapq.heappush(upper_heap, val)
                lower_sum -= val
                upper_sum += val
                lower_size -= 1
                upper_size += 1
            elif lower_size < upper_size:
                clean_heap(upper_heap, False)
                val = heapq.heappop(upper_heap)
                heapq.heappush(lower_heap, -val)
                upper_sum -= val
                lower_sum += val
                upper_size -= 1
                lower_size += 1

        def add_num(num):
            nonlocal lower_sum, upper_sum, lower_size, upper_size
            clean_heap(lower_heap, True)
            if not lower_heap or num <= -lower_heap[0]:
                heapq.heappush(lower_heap, -num)
                lower_sum += num
                lower_size += 1
            else:
                heapq.heappush(upper_heap, num)
                upper_sum += num
                upper_size += 1
            rebalance()

        def remove_num(num):
            nonlocal lower_sum, upper_sum, lower_size, upper_size
            clean_heap(lower_heap, True)
            clean_heap(upper_heap, False)
            
            if lower_heap and num <= -lower_heap[0]:
                lower_sum -= num
                lower_size -= 1
            else:
                upper_sum -= num
                upper_size -= 1
                
            delayed[num] += 1
            rebalance()

        # Populate the first window of size x
        for i in range(x):
            add_num(nums[i])

        clean_heap(lower_heap, True)
        median = -lower_heap[0]
        cost[0] = (median * lower_size - lower_sum) + (upper_sum - median * upper_size)

        # Slide the window across the array
        for i in range(1, n - x + 1):
            remove_num(nums[i - 1])
            add_num(nums[i + x - 1])
            
            clean_heap(lower_heap, True)
            median = -lower_heap[0]
            cost[i] = (median * lower_size - lower_sum) + (upper_sum - median * upper_size)

        # Iterative Bottom-Up DP to select k non-overlapping windows of size x
        m = len(cost)
        prev_dp = [0] * (m + x + 2)
        
        for c in range(1, k + 1):
            curr_dp = [float('inf')] * (m + x + 2)
            for i in range(m - 1, -1, -1):
                option1 = curr_dp[i + 1]
                option2 = cost[i] + prev_dp[i + x]
                curr_dp[i] = min(option1, option2)
            prev_dp = curr_dp
            
        return prev_dp[0]