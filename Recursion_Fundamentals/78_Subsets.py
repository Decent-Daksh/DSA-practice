from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        def helper( i , curr):
            if i == len(nums):
                result.append(curr)
                return
            helper(i+1 , curr)
            helper(i+1 , curr + [nums[i]])
        
        helper( 0 , current)

        return result
