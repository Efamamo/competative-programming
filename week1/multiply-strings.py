class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        carry1 = 1
        
        for i in num1[::-1]: 
            carry2 = 1 
            for j in num2[::-1]:
                res += int(i)*int(j)*carry1*carry2 
                carry2 *= 10 
            carry1 *= 10
        return str(res)

                

            
        
    
        