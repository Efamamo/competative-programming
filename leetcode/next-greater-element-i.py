class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        d = {}
        for i in nums2:
            while st and st[-1]<i:
                d[st.pop()] = i
            st.append(i)
        print(d)
        res = [-1]*len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in d:
                res[i] = d[nums1[i]]
        return res 


        