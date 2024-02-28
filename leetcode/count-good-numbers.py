class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(n,x,m):
            if x== 0:
                return 1
           
            if x%2 == 0:
                return ((power(n,x//2,m))**2)%m
            else:
                return ((power(n,x//2,m)**2)*n)%m
        

        if n%2 == 0:
            return (power(5,n//2,10**9+7)*power(4,n//2,10**9+7))%(10**9+7)
        else:
            return (power(5,n//2+1,10**9+7)*power(4,n//2,10**9+7))%(10**9+7)
        