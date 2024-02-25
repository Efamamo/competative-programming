class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ctr = 0
        st = []
        for i in s:
            if i == "(":
                st.append(i)
            elif st:
                st.pop()
            else:
                ctr += 1
        return ctr + len(st)