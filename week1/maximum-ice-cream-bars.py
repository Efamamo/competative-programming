class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total=0
        count=0
        for i in costs:
            if total+i<=coins:
                count+=1
                total+=i
            else:
                break
        return count

        