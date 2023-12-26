class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter={}
        res=[]
        for i,e in enumerate(arr2):
            counter[e]=i
        
        val=len(arr1)-1
        val=0
        for e in arr1:
            if e not in counter:
                res.append(e)

        for i in res:
            arr1.remove(i) 
        res.sort()      
        for i in range(len(arr1)):
            for j in range(len(arr1)-1):
                if counter[arr1[j]]>counter[arr1[j+1]]:
                    arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
        arr1.extend(res)
        return arr1
        