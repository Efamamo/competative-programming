class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative=[]
        result=[]
        for i in nums:
            if i<0:
                negative.append(i)
            else:
                positive.append(i)
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])
        return result

        