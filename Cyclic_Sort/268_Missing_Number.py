from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == n or nums[i] == i:
                i+=1
            else:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        
        for i in range(n):
            if nums[i] == n or i != nums[i]:
                return i
            else:
                continue

        return n