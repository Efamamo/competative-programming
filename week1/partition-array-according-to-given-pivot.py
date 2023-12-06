class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        idx=nums.index(pivot)
        l=[]
        r=[]
        eq=[]
        for i,e in enumerate(nums):
            if i==idx:
              continue
            if e==pivot:
              eq.append(e)
            elif e<=pivot:
              l.append(e)
            else:
              r.append(e)
        return l+eq+[pivot]+r