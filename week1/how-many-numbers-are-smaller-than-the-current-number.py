class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num=sorted(nums)
        d={}
        for i in range(len(sorted_num)):
            if sorted_num[i] not in d:
                d[sorted_num[i]]=i
        for i in range(len(nums)):
            nums[i]=d[nums[i]]
        return nums
        # for i,element in enumerate(nums):
        #     nums[i]=(e,i)
        # nums.sort()
        # initial=0
        # result=[]
        # for i in range(initial,i):
            

    

        # for i in range(len(nums)):
        #     total=0
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         if nums[j] < nums[i]:
        #             total+=1
        #     result.append(total)
        return result
                
        