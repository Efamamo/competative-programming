class Solution:
    def resolves(self, a, b, Operator):
        if Operator == '+':
            return a + b
        elif Operator == '-':
            return a - b
        elif Operator == '*':
            return a * b
        return int(a / b)

    def evalRPN(self, tokens):
        st = []
        for i in tokens:
            if i in "+-/*":
                b = int(st.pop())
                a = int(st.pop())
                st.append(self.resolves(a,b,i))
            else:
                st.append(i)
        return int(st.pop())


        