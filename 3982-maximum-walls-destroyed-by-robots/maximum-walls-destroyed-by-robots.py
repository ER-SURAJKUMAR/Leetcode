import bisect
from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        # Map original distances to sorted robot positions
        robots_to_distance = {r: d for r, d in zip(robots, distance)}
        robots.sort()
        walls.sort()

        left = [0] * n
        right = [0] * n
        num = [0] * n # Walls between robot i-1 and robot i

        for i in range(n):
            curr_pos = robots[i]
            curr_dist = robots_to_distance[curr_pos]
            
            # --- Left Shot Coverage ---
            # Bound by the previous robot or the bullet distance
            l_bound = curr_pos - curr_dist
            if i > 0:
                l_bound = max(l_bound, robots[i-1] + 1)
            
            l_idx = bisect.bisect_left(walls, l_bound)
            r_idx = bisect.bisect_right(walls, curr_pos)
            left[i] = max(0, r_idx - l_idx)

            # --- Right Shot Coverage ---
            # Bound by the next robot or the bullet distance
            r_bound = curr_pos + curr_dist
            if i < n - 1:
                r_bound = min(r_bound, robots[i+1] - 1)
            
            l_idx_r = bisect.bisect_left(walls, curr_pos)
            r_idx_r = bisect.bisect_right(walls, r_bound)
            right[i] = max(0, r_idx_r - l_idx_r)

            # --- Overlap Zone ---
            # Walls between robot[i-1] and robot[i]
            if i > 0:
                # All walls from robot[i-1]'s position to robot[i]'s position
                p_start = bisect.bisect_left(walls, robots[i-1])
                p_end = bisect.bisect_right(walls, robots[i])
                num[i] = max(0, p_end - p_start)

        # DP State: max unique walls destroyed
        # sub_left: max walls if current robot i fires LEFT
        # sub_right: max walls if current robot i fires RIGHT
        sub_left, sub_right = left[0], right[0]

        for i in range(1, n):
            # If current fires Left: 
            # 1. Previous fired Left + current fires Left
            # 2. Previous fired Right + current fires Left (adjust for shared walls in 'num')
            current_left = max(
                sub_left + left[i],
                sub_right - right[i-1] + min(left[i] + right[i-1], num[i])
            )
            
            # If current fires Right:
            # It doesn't conflict with previous robot's choice
            current_right = max(sub_left + right[i], sub_right + right[i])
            
            sub_left, sub_right = current_left, current_right

        return max(sub_left, sub_right)