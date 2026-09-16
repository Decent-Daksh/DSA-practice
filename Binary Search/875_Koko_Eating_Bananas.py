from typing import List
import math
class Solution:
    def minEatingSpeed(self,piles:List[int],h:int)->int:
        def hoursNeeded(k:int):
            total =0
            for pile in piles:
                total += math.ceil(pile/k)
            return total
        l , r = 0, max(piles)
        answer = r
        while l <= r:
            mid = l +(r-l)//2
            if hoursNeeded(mid)<=h:
                answer = mid
                r = mid-1
            else:
                l = mid+1
        return answer
