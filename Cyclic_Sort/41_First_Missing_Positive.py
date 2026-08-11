from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        i = 0
        n = len(nums)
        while i < n:
            if  nums[i] > n or nums[i] < 1 or nums[i] == i+1 or nums[i] == nums[nums[i] -1] :
                i+=1
            else:
                nums[nums[i]-1],nums[i] = nums[i] , nums[nums[i]-1]
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        
        return n+1