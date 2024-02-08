class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=0
        max_vowls=0
        length=0
        vowels={"a","e","i","o","u"}
        for r in range(len(s)):
            if r-l==k:
                if s[l] in vowels:
                    length-=1
                l+=1
            if s[r] in vowels:
                length+=1
            
            max_vowls=max(max_vowls,length)
        return max_vowls
            
                

        