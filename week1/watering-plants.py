class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps=0
        val=capacity
        for i,e in enumerate(plants):
            if val>=e:
                val-=e
            else:
                steps+=(2*i)
                val=capacity
                val-=e
            steps+=1
        return steps


        