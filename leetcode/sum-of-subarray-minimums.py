class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        st = []
        res = 0
        for i in range(len(arr)):
            if not st:
                st.append(i)
            else:
                while st and arr[i] < arr[st[-1]]:
                    val = st.pop()
                    start = val-(-1) if not st else val-st[-1]
                    res += (start)*(i-val)*arr[val]
                
                st.append(i)
            
            
        while st:
            val = st.pop()
            start = val-(-1) if not st else val-st[-1]
            res += (start)*(len(arr)-val)*arr[val]
            
        return res%(10**9+7)


                


        