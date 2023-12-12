class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        merge=set(fronts+backs)
        for i in range(len(fronts)):
            if fronts[i]== backs[i] and fronts[i] in merge:
                merge.remove(fronts[i])
        if merge:
            return min(merge)
        return 0
        
