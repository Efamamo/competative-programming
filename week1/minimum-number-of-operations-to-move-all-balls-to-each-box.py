class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result=[0]*len(boxes)
        for i in range(len(boxes)):
            count=0
            l=i-1
            r=i+1
            while l>=0 and r<len(boxes):
                if boxes[l]=="1":
                    count+=abs(i-l)
                if boxes[r]=="1":
                    count+=abs(i-r)
                l-=1
                r+=1
            while l>=0:
                if boxes[l]=="1":
                    count+=abs(i-l)
                l-=1
            while r<len(boxes):
                if boxes[r]=="1":
                    count+=abs(i-r)
                r+=1

            result[i]=count
        return result
            

        

        
        