# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        k =0
        current = head
        while current:
            k+=1
            current = current.next
        res = []
        current = head
        i=0
        while current:
            if k%2 == 0:
                if i==k//2:
                    return current
            else:
                if i==k//2:
                    return current
            
            i+=1
            current = current.next
        
        
        