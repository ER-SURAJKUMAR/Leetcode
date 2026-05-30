from sortedcontainers import SortedList

class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (4 * size)

    def update(self, index, value, node, start, end):
        if start == end:
            self.tree[node] = value
            return
        mid = (start + end) // 2
        if index <= mid:
            self.update(index, value, 2 * node, start, mid)
        else:
            self.update(index, value, 2 * node + 1, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, q_start, q_end, node, start, end):
        if q_start > end or q_end < start:
            return 0
        if q_start <= start and end <= q_end:
            return self.tree[node]
        mid = (start + end) // 2
        left_max = self.query(q_start, q_end, 2 * node, start, mid)
        right_max = self.query(q_start, q_end, 2 * node + 1, mid + 1, end)
        return max(left_max, right_max)

class Solution:
    def getResults(self, queries: list[list[int]]) -> list[bool]:
        # Determine the maximum coordinate size needed for the Segment Tree
        max_x = 0
        for q in queries:
            max_x = max(max_x, q[1])
        
        # Segment tree size will be max_x + 2 to safely handle indices
        n = max_x + 2
        seg_tree = SegmentTree(n)
        
        # SortedList keeps track of obstacles. 
        # Initialize with 0 (origin) and an upper bound beyond any query x.
        obstacles = SortedList([0, n])
        
        # Initially, the gap at 'n' from 0 is 'n'
        seg_tree.update(n, n, 1, 0, n - 1)
        
        results = []
        
        for q in queries:
            if q[0] == 1:
                x = q[1]
                # Find where x fits among existing obstacles
                idx = obstacles.bisect_left(x)
                prev_x = obstacles[idx - 1]
                next_x = obstacles[idx]
                
                # Insert the new obstacle
                obstacles.add(x)
                
                # Update segment tree with the two new split gaps
                seg_tree.update(x, x - prev_x, 1, 0, n - 1)
                seg_tree.update(next_x, next_x - x, 1, 0, n - 1)
                
            elif q[0] == 2:
                x, sz = q[1], q[2]
                
                # Find the closest obstacle strictly to the left of x
                idx = obstacles.bisect_right(x)
                prev_x = obstacles[idx - 1]
                
                # Option 1: Maximum full gap fully contained within [0, x]
                max_gap = seg_tree.query(0, x, 1, 0, n - 1)
                
                # Option 2: The remaining space between the last obstacle before x and x itself
                current_tail_gap = x - prev_x
                
                actual_max_space = max(max_gap, current_tail_gap)
                
                results.append(actual_max_space >= sz)
                
        return results