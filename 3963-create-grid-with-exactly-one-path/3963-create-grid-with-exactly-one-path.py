class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        # Initialize the grid filled with obstacles '#'
        g = [['#'] * n for _ in range(m)]
        
        # Open up the entire first row
        g[0] = ['.'] * n
        
        # Open up the entire last column
        for i in range(m):
            g[i][-1] = '.'
            
        return ["".join(row) for row in g]