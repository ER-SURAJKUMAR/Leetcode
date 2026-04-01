class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        # Pair everything with original indices to preserve order at the end
        combined = []
        for i in range(len(positions)):
            combined.append([positions[i], healths[i], directions[i], i])
        
        # Sorting by position is required to simulate the line movement
        combined.sort()
        
        stack = []
        for i in range(len(combined)):
            if combined[i][2] == 'R':
                stack.append(combined[i])
            else:
                # Current robot is 'L', check for collisions with 'R' robots in stack
                while stack and stack[-1][2] == 'R' and combined[i][1] > 0:
                    if stack[-1][1] < combined[i][1]:
                        # Left-moving robot wins
                        stack.pop()
                        combined[i][1] -= 1
                    elif stack[-1][1] > combined[i][1]:
                        # Right-moving robot wins
                        stack[-1][1] -= 1
                        combined[i][1] = 0
                    else:
                        # Both destroyed
                        stack.pop()
                        combined[i][1] = 0
                
                if combined[i][1] > 0:
                    stack.append(combined[i])
        
        # Sort by original index to return healths in initial input order
        stack.sort(key=lambda x: x[3])
        
        return [robot[1] for robot in stack]