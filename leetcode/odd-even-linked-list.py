# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur1 = ListNode()
        dummy2 = cur2 = ListNode()

        cur= head
        while cur and cur.next:
            cur1.next = cur
            cur2.next = cur.next
            cur1 = cur1.next
            cur2 = cur2.next
            cur = cur.next.next
            cur1.next = None
            cur2.next = None
        if cur:
            cur1.next = cur
            cur1 = cur1.next
        cur1.next = dummy2.next
        return dummy.next
            

        