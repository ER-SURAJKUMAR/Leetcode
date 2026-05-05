# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # 1. Compute the length of the list
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
            
        # 2. Connect the tail to the head to make it circular
        tail.next = head
        
        # 3. Find the actual number of steps to the new tail
        # If length is 5 and k is 2, the new tail is at index (5 - 2 - 1) = 2
        k = k % length
        steps_to_new_tail = length - k - 1
        
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
            
        # 4. Break the circular link
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head