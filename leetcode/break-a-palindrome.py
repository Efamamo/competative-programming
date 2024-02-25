class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        arr = []
        for i in palindrome:
            arr.append(i)
            
        for i in range(len(arr)):
            if i == len(arr)//2:
                continue
            elif arr[i]!="a":
                arr[i] = "a"
                return "".join(arr)
        arr[-1] = "b"
        return "".join(arr)
            
        
        