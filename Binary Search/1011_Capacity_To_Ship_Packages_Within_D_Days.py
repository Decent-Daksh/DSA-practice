from typing import List
class Solution:
    def ship_in_min_days(self,weights:List[int],days:int)->int:
        def days_needed(cap:int):
            t_days =1
            curr_load = 0
            for weight in weights:
                if curr_load >= cap:
                    t_days+=1
                    curr_load = 0
                curr_load += weight
            return t_days
        l , r = max(weights) , sum(weights)
        answer = l
        while l <=r :
            mid = l +(r-l)//2
            day = days_needed(mid)
            if day<=days:
                r = mid -1
                answer = mid
            else:
                l = mid +1
        return answer

