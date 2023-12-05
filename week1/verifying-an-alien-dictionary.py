class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        word=words[0]
        min_w=min(words,key=len)
        for i in words:
            min_len=min(len(word),len(i))
            for j in range(min_len):
                if order.index(i[j])>order.index(word[j]):
                    break
                if order.index(i[j])==order.index(word[j]):
                    continue
                else:
                    return False
            else:
                if len(i)<len(word):
                    return False
            word=i
                
        return True
    

        
        