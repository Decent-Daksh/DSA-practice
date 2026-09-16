from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums)-1
        while l<=r:
            mid = l +(r-l)//2
            if nums[mid] == target:
                return mid
            if nums[l]<= nums[mid]:
                if nums[l]<=target<nums[mid]:
                    right = mid -1
                else:
                    left = mid +1
            else:
                if nums[mid]< target <= nums[r]:
                    left = mid +1
                else:
                    right = mid - 1
        return -1
