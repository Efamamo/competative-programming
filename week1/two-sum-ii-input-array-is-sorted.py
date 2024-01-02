class Solution(object):
    def twoSum(self, numbers, target):
        i=0
        j=len(numbers)-1
        while i<j:
            sum=numbers[i]+numbers[j]
            if sum==target:
                return [i+1,j+1]
            elif sum>target:
                j-=1
            else:
                i+=1
            
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        