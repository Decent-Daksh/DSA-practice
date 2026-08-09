from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[1])
        count=0
        last_end = intervals[0][1]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0]>=last_end:
                last_end = curr[1]
            else:
                count+=1
        return count
