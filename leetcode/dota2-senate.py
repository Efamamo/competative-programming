class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue1 = deque()
        queue2 = deque()
        n = len(senate)
        for i in range(len(senate)):
            if senate[i] == "D":
                queue1.append(i)
            else:
                queue2.append(i)
        
        while queue1 and queue2:
            if queue1[0]>queue2[0]:
                queue2.append(n)
            else:
                queue1.append(n)
            queue1.popleft()
            queue2.popleft()
            n+=1
        if queue1:
            return "Dire"
        return "Radiant"
        
        


        
        
        


        