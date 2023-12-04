class Solution:
    def largestGoodInteger(self, num: str) -> str:
        subs=[]
        sub=num[0]
        for i in range(1,len(num)):
            if num[i-1]==num[i]:
                sub+=num[i]
            else:
                subs.append(sub)
                sub=num[i]
        subs.append(sub)
        max_sub=""
        int_sub=""
        for i in subs:
            if len(i)>=3 and i[0]>int_sub:
                max_sub=i
                int_sub=i[0]
        return max_sub[:3]
        