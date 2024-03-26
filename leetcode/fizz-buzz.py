class Solution(object):
    def fizzBuzz(self, n):
        res = []
        for i in range(1,n+1):
            if not (i%3 or i%5):
                res.append("FizzBuzz")
            elif not i%3:
                res.append("Fizz")
            elif not i%5:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
        """
        :type n: int
        :rtype: List[str]
        """
        