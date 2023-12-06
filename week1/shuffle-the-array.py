class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result=[]
        i=0
        while i<n and n<len(nums):
            result.append(nums[i])
            result.append(nums[n])
            i+=1
            n+=1
        return result

        