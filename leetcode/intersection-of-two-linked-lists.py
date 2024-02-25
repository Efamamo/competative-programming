# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        current1 = headA
        current2 = headB
        while headA and headB:
            if current1 == current2:
                return current1
            if not current1:
                current1 = headB
            else:
                current1 = current1.next
            if not current2:
                current2 = headA
            else:
                current2 = current2.next
                
        
      
        