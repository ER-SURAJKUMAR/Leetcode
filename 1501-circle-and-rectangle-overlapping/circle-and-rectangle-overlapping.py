class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the point in the rectangle closest to the circle's center
        nearest_x = max(x1, min(xCenter, x2))
        nearest_y = max(y1, min(yCenter, y2))
        
        # Calculate squared distance from center to the nearest point
        dx = xCenter - nearest_x
        dy = yCenter - nearest_y
        
        # Compare squared distance with squared radius
        return (dx * dx + dy * dy) <= (radius * radius)