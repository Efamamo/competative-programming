class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        flag = False
        for i in count:
            if count[i] % 2 == 0:
                res += count[i]
                
            if count[i] % 2 != 0 :
                if count[i] > 2 :
                    res += count[i]-1
                flag = True
        if flag:
            return res + 1
        return res
            
            
        
        
        