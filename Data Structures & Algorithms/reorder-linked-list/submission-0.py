# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle of list, slow becomes middle
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None

    
        #reverse rhs
        prev = None
        current = second

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        #move through each side and set next pointers

        p2 = prev
        p1 = head

        while p1 and p2:
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2
        






        
            


        