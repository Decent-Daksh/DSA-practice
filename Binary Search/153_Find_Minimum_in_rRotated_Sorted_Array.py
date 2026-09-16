from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums)-1
        min_v= float('inf')
        while l<=r:
            mid = l + (r-l)//2
            min_v =min(min_v,nums[mid])
            if nums[mid]> nums[r]:
                l = mid +1
            else:
                r = mid-1
        return min_v