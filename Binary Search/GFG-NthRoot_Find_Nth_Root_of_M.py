
class Solution:
    def find_nth_root(self,n:int,m:int)->int:
        l , r = 0,m
        while l<=r:
            mid = l +(r-l)//2
            if mid**n==m:
                return mid
            if mid**n>m:
                r= mid -1
            else:
                l= mid +1
        return -1