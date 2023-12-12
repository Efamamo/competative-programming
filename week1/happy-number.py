class Solution:
    def isHappy(self, n: int) -> bool:
        set_of_no=set()
        while n!=1: 
            n=sum([int(i)**2 for i in str(n)]) 
            if n in set_of_no:
                return False
            set_of_no.add(n)
        return True
            
        

        