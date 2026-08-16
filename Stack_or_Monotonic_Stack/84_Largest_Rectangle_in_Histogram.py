from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        bucket =[]
        heights.append(0)
        largest = 0
        for i in range(len(heights)):
            while bucket and  heights[bucket[-1]] > heights[i]:
                temp = bucket[-1]
                bucket.pop()
                weight = i if not bucket else i - bucket[-1] -1
                height = heights[temp]
                area = height * weight
                largest = max(area , largest)
            bucket.append(i)
       
        return largest