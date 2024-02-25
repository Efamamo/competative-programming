class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        phar={"]":"[","}":"{",")":"("}
        st=[]
        for i in s:
            if i in phar.values():
                st.append(i)
            else:
                if not st:
                    return False
                elif phar[i]!=st.pop():
                    return False

        if st:
            return False
        return True

        