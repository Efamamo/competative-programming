class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        count_1=0
        count_0=0
       
        for i in nums:
            if i==1:
                count_1+=1
        maxim=count_1+count_0
        result=[0]
        for i in range(1,len(nums)):
            if nums[i-1]==0:
                count_0+=1
            else:
                count_1-=1
            add=count_0+count_1
            if add>maxim:
                maxim=add
                result=[i]
            elif add==maxim:
                result.append(i)
        count_0=0
        for i in nums:
            if i==0:
                count_0+=1
        if count_0>maxim:
            result=[len(nums)]
        elif count_0==maxim:
            result.append(len(nums))
        

        return result
        
        