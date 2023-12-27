class Solution(object):
    def intersect(self, nums1, nums2):
        num=[0]*9
        arr=[]
        for i in nums2:
            if i in nums1:
                arr.append(i)
                nums1[nums1.index(i)]=""
        return arr
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        