#this is the vesion with heap using time complexity o(n logk)
import heapq
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        asset ={}
        for num in nums:
            asset[num] = asset.get(num , 0) + 1
        min_heap = []
        for num , freq in asset.items():
            heapq.heappush(min_heap,(freq,num))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        result = []
        for i in range(k):
            temp = heapq.heappop(min_heap)
            result.append(temp[1])
        return result
# the bucket sort version with the time complexity O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        asset ={}
        for num in nums:
            asset[num] = asset.get(num , 0) + 1
        bucket = [[] for i in range(len(nums) +1)]
        for num,freq in asset.items():
            bucket[freq].append(num)
        result = []
        for i in range(len(bucket)-1 , 0 ,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result)==k:
                    return result

        return result
