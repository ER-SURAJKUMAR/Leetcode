# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        idx = 1
        
        first_critical = -1
        prev_critical = -1
        min_dist = float('inf')
        
        while curr and curr.next:
            # Check for local maxima or local minima
            is_maxima = prev.val < curr.val and curr.val > curr.next.val
            is_minima = prev.val > curr.val and curr.val < curr.next.val
            
            if is_maxima or is_minima:
                if first_critical == -1:
                    first_critical = idx
                else:
                    min_dist = min(min_dist, idx - prev_critical)
                
                prev_critical = idx
            
            prev = curr
            curr = curr.next
            idx += 1
        
        # If fewer than 2 critical points were found
        if first_critical == -1 or first_critical == prev_critical:
            return [-1, -1]
        
        max_dist = prev_critical - first_critical
        return [min_dist, max_dist]