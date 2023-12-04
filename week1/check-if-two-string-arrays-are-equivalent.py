class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        words1=""
        words2=""
        for i in word1:
            words1+=i
        for j in word2:
            words2+=j
        if words1==words2:
            return True
        return False
        