class Solution(object):
    def romanToInt(self, s):
        Roman_numericals={

        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M":1000}
        total=0
        previous_value=0
        for i in s[::-1]:
            value =Roman_numericals[i]
            if value<previous_value:
                total-=value
            else:
                total+=value
            previous_value=value
        return total


        """
        :type s: str
        :rtype: int
        """