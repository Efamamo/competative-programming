class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word=min(strs,key=len)
        for i in range(len(word)):
            for j in range(len(strs)):
                if strs[j][i]!=word[i]:
                    return word[:i]
        return word

        