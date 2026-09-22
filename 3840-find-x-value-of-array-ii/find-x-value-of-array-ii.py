class Node:
    def __init__(self, k: int):
        self.k = k
        self.prod = 1
        self.remain = [0] * k

class SegmentTree:
    def __init__(self, nums: list[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree = [Node(k) for _ in range(4 * self.n)]
        self._build(nums, 0, 0, self.n - 1)

    def _merge(self, left: Node, right: Node) -> Node:
        res = Node(self.k)
        res.prod = (left.prod * right.prod) % self.k
        
        # Prefixes within the left segment
        for i in range(self.k):
            res.remain[i] = left.remain[i]
            
        # Prefixes extending into the right segment
        for i in range(self.k):
            rem = (left.prod * i) % self.k
            res.remain[rem] += right.remain[i]
            
        return res

    def _build(self, nums: list[int], idx: int, l: int, r: int):
        if l == r:
            val = nums[l] % self.k
            self.tree[idx].prod = val
            self.tree[idx].remain[val] = 1
            return
        
        mid = (l + r) // 2
        self._build(nums, 2 * idx + 1, l, mid)
        self._build(nums, 2 * idx + 2, mid + 1, r)
        self.tree[idx] = self._merge(self.tree[2 * idx + 1], self.tree[2 * idx + 2])

    def update(self, idx: int, l: int, r: int, pos: int, val: int):
        if l == r:
            v = val % self.k
            self.tree[idx].prod = v
            self.tree[idx].remain = [0] * self.k
            self.tree[idx].remain[v] = 1
            return
        
        mid = (l + r) // 2
        if pos <= mid:
            self.update(2 * idx + 1, l, mid, pos, val)
        else:
            self.update(2 * idx + 2, mid + 1, r, pos, val)
        self.tree[idx] = self._merge(self.tree[2 * idx + 1], self.tree[2 * idx + 2])

    def query(self, idx: int, l: int, r: int, ql: int, qr: int) -> Node:
        if ql <= l and r <= qr:
            return self.tree[idx]
        
        mid = (l + r) // 2
        if qr <= mid:
            return self.query(2 * idx + 1, l, mid, ql, qr)
        if ql > mid:
            return self.query(2 * idx + 2, mid + 1, r, ql, qr)
            
        left_node = self.query(2 * idx + 1, l, mid, ql, qr)
        right_node = self.query(2 * idx + 2, mid + 1, r, ql, qr)
        return self._merge(left_node, right_node)


class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        tree = SegmentTree(nums, k)
        ans = []
        
        for idx, val, start, x in queries:
            tree.update(0, 0, n - 1, idx, val)
            res_node = tree.query(0, 0, n - 1, start, n - 1)
            ans.append(res_node.remain[x])
            
        return ans