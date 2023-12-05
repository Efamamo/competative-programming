class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        def valid(word,row):
            for i in word:
                if i.lower() not in row:
                    return False
            return True
        result=[]
        for i in words:
            if valid(i,row1) or valid(i,row2) or valid(i,row3):
                result.append(i)
        return result


    

                


        