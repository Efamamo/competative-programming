class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        initial=float("inf")
        second=float("inf")
        for num in nums:
            if num<=initial:
                initial=num
            elif num<=second:
                second=num
            else:
                return True
        return False