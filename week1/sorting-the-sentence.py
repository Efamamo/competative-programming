class Solution:
    def sortSentence(self, s: str) -> str:
        s_arr=s.split()
        s_arr.sort(key= lambda x:x[-1])
        return " ".join(x[:len(x)-1] for x in s_arr)



        