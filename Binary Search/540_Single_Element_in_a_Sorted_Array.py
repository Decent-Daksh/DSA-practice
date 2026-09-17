from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l , r = 0 , len(nums)-1
        while l<=r:
            mid= l +(r-l)//2
            left_ok = (0 <= mid - 1 < len(nums)) and nums[mid] == nums[mid - 1]
            right_ok = (0 <= mid + 1 < len(nums)) and nums[mid] == nums[mid + 1]

            if not left_ok and not right_ok:
                return nums[mid]
        
                

            if mid%2==0:
                if (0<=mid+1<len(nums)) and nums[mid]!=nums[mid+1]:
                    r = mid-1
                else:
                    l = mid+2
            else:
                if (0<=mid-1<len(nums))  and nums[mid]!=nums[mid-1]:
                    r = mid-1
                else:
                    l = mid +1

