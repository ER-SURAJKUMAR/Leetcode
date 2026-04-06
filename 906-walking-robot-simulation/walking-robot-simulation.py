class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # Directions: 0: North, 1: East, 2: South, 3: West
        # Corresponding (dx, dy)
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        # Initial position and direction (North)
        x, y = 0, 0
        direction = 0
        
        # Convert obstacles to a set for O(1) lookups
        obstacle_set = set(map(tuple, obstacles))
        
        max_dist_sq = 0
        
        for cmd in commands:
            if cmd == -2:  # Turn left
                direction = (direction - 1) % 4
            elif cmd == -1:  # Turn right
                direction = (direction + 1) % 4
            else:
                # Move forward k units
                for _ in range(cmd):
                    next_x = x + dx[direction]
                    next_y = y + dy[direction]
                    
                    if (next_x, next_y) not in obstacle_set:
                        x, y = next_x, next_y
                        # Update max distance squared at each step
                        max_dist_sq = max(max_dist_sq, x*x + y*y)
                    else:
                        # Hit an obstacle, stop moving for this command
                        break
                        
        return max_dist_sq