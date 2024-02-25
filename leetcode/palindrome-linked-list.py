# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        l = 0
        r = len(arr)-1
        while r>l:
            if arr[l]!=arr[r]:
                return False
            l+=1
            r-=1
        return True
        