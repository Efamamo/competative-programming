# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = dummy1 = ListNode()
        greater = dummy2 = ListNode()
        cur = head
        while cur:
            if cur.val < x:
                less.next = cur
                cur = cur.next
                less = less.next
                less.next = None
            else:
                greater.next = cur
                cur = cur.next
                greater = greater.next
                greater.next = None
        less.next = dummy2.next
        return dummy1.next

        