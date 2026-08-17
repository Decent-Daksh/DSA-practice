class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = - n
        if n == 0:
            return 1
        half = self.myPow(x, n//2)
        if n%2 == 0:
            ans = half*half
        else:
            ans = half * half * x
        
        return ans
        

        