# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        prev = None
        i = 0
        while fast and i<n:
            fast = fast.next
            i+=1
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        print(slow.val)
        if prev == None:
            head = head.next
        else:
            prev.next = slow.next
        return head
        
        
            
        