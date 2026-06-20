class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        # Step 1: Add boundary restrictions
        # Building 1 must have height 0.
        # Building n can at most have height n - 1 if there are no constraints.
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        
        # Step 2: Sort restrictions by building ID
        restrictions.sort()
        
        m = len(restrictions)
        
        # Step 3: Left-to-Right Pass
        # A building's height cannot exceed the previous building's height + their distance
        for i in range(1, m):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]
            restrictions[i][1] = min(h2, h1 + (id2 - id1))
            
        # Step 4: Right-to-Left Pass
        # A building's height cannot exceed the next building's height + their distance
        for i in range(m - 2, -1, -1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i + 1]
            restrictions[i][1] = min(h1, h2 + (id2 - id1))
            
        # Step 5: Find the maximum peak between any two adjacent restricted buildings
        max_tallest = 0
        for i in range(m - 1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i + 1]
            
            # Theoretical highest peak reachable between id1 and id2
            peak = (h1 + h2 + (id2 - id1)) // 2
            max_tallest = max(max_tallest, peak)
            
        return max_tallest