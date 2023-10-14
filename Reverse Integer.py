class Solution(object):
    def reverse(self, x):
        if x<0:
            x=-1*x
            str_num=str(x)
            final=""
            for i in range(len(str_num)-1,-1,-1):
                final+=str_num[i]
            ans=int(final)
            if (-2)**31 <= ans <= (2**31)-1:

                return -1*ans
            return 0

            
        else:
            str_num=str(x)
            final=""
            for i in range(len(str_num)-1,-1,-1):
                final+=str_num[i]
            ans=int(final)
            if (-2)**31<=ans<=(2)**31-1:
            
                return ans
            return 0

        

        """
        :type x: int
        :rtype: int
        """
        
