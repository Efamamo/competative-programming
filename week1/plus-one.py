class Solution(object):
    def plusOne(self, digits):
        total=''
        List=[]
        for i in digits:
            i=str(i)
            total+=i
        total=int(total)
        total+=1
        total=str(total)
        for i in total:
            i=int(i)
            List.append(i)
        return List

        """
        :type digits: List[int]
        :rtype: List[int]
        """