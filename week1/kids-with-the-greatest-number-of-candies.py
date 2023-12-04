class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bools=[True]*len(candies)
        maxim=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies<maxim:
                bools[i]=False
        return bools

        