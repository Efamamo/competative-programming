class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        count=0
        mini=float('inf')
        if len(nums1)>len(nums2):
            s=set(nums1)
            for i in nums2:
                if i in s:
                    mini=min(mini,i)
        else:
            s=set(nums2)
            for i in nums1:
                if i in s:
                    mini=min(mini,i)
        return mini if mini!=float('inf') else -1

        