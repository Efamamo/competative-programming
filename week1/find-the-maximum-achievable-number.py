class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        for i in range(t*2):
            num+=1
        return num
        