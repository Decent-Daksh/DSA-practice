from typing import List
class Solution:


    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged =[]
        intervals.sort(key = lambda x: x[0])
        
        for i in range(len(intervals)):
            curr = intervals[i]
            if merged and  curr[0]<=merged[-1][1]:
                merged[-1][1] = max(curr[1], merged[-1][1])
            else:
                merged.append(curr)
        
        return merged