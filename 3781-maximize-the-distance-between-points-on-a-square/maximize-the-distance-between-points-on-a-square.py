import bisect

class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        # Step 1: 1D Transformation
        dists = []
        for x, y in points:
            if y == 0: dists.append(x)
            elif x == side: dists.append(side + y)
            elif y == side: dists.append(3 * side - x)
            else: dists.append(4 * side - y)
        
        dists.sort()
        n = len(dists)
        perimeter = 4 * side

        def check(mid):
            # Only check starting points in the first interval
            # If we can't find a valid sequence starting early, we won't find one later
            limit = dists[0] + perimeter // k
            for i in range(n):
                if dists[i] > limit:
                    break
                
                count = 1
                curr_pos = dists[i]
                first_pos = dists[i]
                
                # Greedy pick k-1 more points using binary search to jump
                for _ in range(k - 1):
                    # Find the next point at least 'mid' distance away
                    idx = bisect.bisect_left(dists, curr_pos + mid)
                    if idx == n:
                        count = -1 # Not enough points left
                        break
                    curr_pos = dists[idx]
                    count += 1
                
                # Check circular distance back to start
                if count == k and (perimeter - (curr_pos - first_pos)) >= mid:
                    return True
            return False

        # Step 2: Binary Search on the Answer
        low = 1
        high = side # Max Manhattan dist on a square is 2*side, but min-max is limited
        ans = 1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans