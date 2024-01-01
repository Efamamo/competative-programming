class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:

        tasks.sort()
        processorTime.sort()
        print(tasks)
        i=0
        j=0
        k=len(processorTime)-1
        res=[]
        while i<len(tasks):
            maxim=0
            for j in range(4):
                maxim=max(maxim,processorTime[k]+tasks[i])
                i+=1
            res.append(maxim)
            k-=1
       
        if res:
            return max(res)
            

    
            
        