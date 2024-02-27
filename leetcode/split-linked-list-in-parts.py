# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        res = []

        if length>=k:
            rem = length%k
            parts = length//k
            current = head
            
            while current:
                i = 0
                cur_h = current
                cur_v = 0
                while current and i<parts:
                    current = current.next
                    i+=1
                    cur_v+=1
                if rem:
                    k = current
                    current = current.next
                    cur_v+=1
                    rem-=1
                res.append(cur_h)

                h = cur_h
                j = 0
                while h.next and j<cur_v-1:
                    h = h.next
                    j+=1
                h.next = None
                

               
                
        else:
            current = head
            i = 0
            while current:
                val = current
                res.append(val)
                current = current.next
                val.next = None
                i+=1
            while i<k:
                res.append(None)
                i+=1
        
      
        return res
        