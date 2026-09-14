class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # Check if there is overlap on both X and Y axes
        overlap_x = rec1[0] < rec2[2] and rec1[2] > rec2[0]
        overlap_y = rec1[1] < rec2[3] and rec1[3] > rec2[1]
        
        return overlap_x and overlap_y