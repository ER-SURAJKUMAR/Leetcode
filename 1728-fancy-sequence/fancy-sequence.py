class Fancy:
    def __init__(self):
        self.mod = 10**9 + 7
        self.seq = []
        self.a = 1  # Global multiplier
        self.b = 0  # Global increment

    def append(self, val: int) -> None:
        # We want: (stored_val * a + b) % mod == val
        # So: stored_val = (val - b) * inv(a) % mod
        # pow(self.a, self.mod - 2, self.mod) gives the modular inverse of a
        inv_a = pow(self.a, self.mod - 2, self.mod)
        self.seq.append(((val - self.b) * inv_a) % self.mod)

    def addAll(self, inc: int) -> None:
        # Update global increment: (a * x + b) + inc
        self.b = (self.b + inc) % self.mod

    def multAll(self, m: int) -> None:
        # Update both global factors: m * (a * x + b) -> (m * a) * x + (m * b)
        self.a = (self.a * m) % self.mod
        self.b = (self.b * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        # Apply the current global transformation to the stored value
        return (self.seq[idx] * self.a + self.b) % self.mod