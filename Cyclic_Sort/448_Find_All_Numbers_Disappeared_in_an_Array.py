from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == i+1 or nums[i] == nums[nums[i]-1]:
                i+=1
            else:
                nums[nums[i] -1],nums[i] = nums[i] , nums[nums[i] -1]
        
        for i in range(n):
            if not nums[i] == i+1 :
                result.append(i+1)
            else:
                continue
        
        return result