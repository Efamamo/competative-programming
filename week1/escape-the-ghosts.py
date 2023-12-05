class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dis= abs(target[0]) + abs(target[1])
        g_dis=0
        for i in ghosts:
            g_dis=abs(target[0]-i[0]) + abs(target[1]-i[1])
            if g_dis<=dis:
                return False
        return True

        