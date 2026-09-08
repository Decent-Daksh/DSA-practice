from typing import List
class Solution:
    def insertPosition(self,nums:List[int] , target:int) -> int:
        left, right = 0 , len(nums)-1
        pos =0
        while(left<=right):
            mid  = left +(right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left = mid+1
                
            else:
                right =mid -1
                
        return left