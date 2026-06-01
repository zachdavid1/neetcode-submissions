# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast_pointer= head
        slow_pointer = head
        if head:
            if head.next:
                while fast_pointer!=None:
                    fast_pointer = fast_pointer.next
                    if fast_pointer:
                        fast_pointer = fast_pointer.next
                    slow_pointer = slow_pointer.next
                    if fast_pointer == slow_pointer:
                        return True


        return False
        