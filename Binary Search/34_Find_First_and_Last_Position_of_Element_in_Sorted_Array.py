from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = right = -1
        l1 , r1 = 0 , len(nums)-1
        while l1<=r1:
            mid = l1 +(r1-l1)//2
            if nums[mid] == target:
                left = mid
                r1 = mid-1
            elif nums[mid]<target:
                l1 = mid+1
            else:
                r1 = mid-1
        l2 , r2 = 0 , len(nums)-1
        while l2<=r2:
            mid = l2 +(r2-l2)//2
            if nums[mid] == target:
                right = mid
                l2 = mid+1
            elif nums[mid]<target:
                l2 = mid+1
            else:
                r2 = mid-1
        return [left, right]