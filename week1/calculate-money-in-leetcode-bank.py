class Solution:
    def totalMoney(self, n: int) -> int:
        result=0
        increament=1
        initial_increment=1
        for i in range(n):
            if i!=0 and i%7==0:
                initial_increment+=1
                increament=initial_increment
            result+=increament
            increament+=1
        return result
            


            

        