class Solution(object):
    def addSpaces(self, s, spaces):
        sp=[]
        space=set(spaces)
        for i,e in enumerate(s):
            if i in space:
                sp.append(" ")   
            sp.append(e)
            
        return "".join(sp)
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
