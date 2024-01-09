class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        my_chars=set()
        max_wind=0
        for r in range(len(s)):
            while s[r] in my_chars:
                my_chars.remove(s[l])
                l+=1
            my_chars.add(s[r])
            max_wind=max(max_wind,r-l+1)
        return max_wind
        

        