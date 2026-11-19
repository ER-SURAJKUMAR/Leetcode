from typing import List


class Solution:

    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()

        # Case 1: Remove 2 smallest elements (new min is nums[2], max is nums[-1])
        case1 = nums[-1] - nums[2]

        # Case 2: Remove 2 largest elements (min is nums[0], new max is nums[-3])
        case2 = nums[-3] - nums[0]

        # Case 3: Remove 1 smallest and 1 largest (new min is nums[1], new max is nums[-2])
        case3 = nums[-2] - nums[1]

        return min(case1, case2, case3)