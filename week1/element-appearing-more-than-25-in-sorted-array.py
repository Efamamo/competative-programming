class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter={}
        for i in arr:
            counter[i]=1+counter.get(i,0)
        n=len(arr)//4
        for i in counter:
            if counter[i]>n:
                return i
        