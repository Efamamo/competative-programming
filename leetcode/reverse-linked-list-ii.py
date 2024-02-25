# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        current = head
        leftP = dummy
        for i in range(left-1):
            leftP = current
            current = current.next
        
        prev = None
        for i in range(right-left+1):
            Next = current.next
            current.next = prev
            prev = current
            current = Next
        
        leftP.next.next = current
        leftP.next = prev
       

        return dummy.next
       
        

        